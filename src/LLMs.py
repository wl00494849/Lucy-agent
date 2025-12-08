from openai import OpenAI
from pydantic import BaseModel
from openai.types.chat import ChatCompletionMessageFunctionToolCall,ChatCompletion
from src.tool.dispatch import DISPATCH
from src.tool.tool_dsc import TOOLS
from src.reader import markdownReader
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import os

class LLMs:
    class LineBot_Requset(BaseModel):
        message:str
        userID:str

    def __init__(self,api_key:str="",defult_model:str=""):
        self.__api_key = os.getenv("OPENAI_API_KEY") or api_key
        self.defult_model = defult_model or "gpt-5.1"
        self.client = OpenAI(api_key=self.__api_key)
        self.memory = []
        self.time = datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f"""
        LLMs(Model={self.defult_model})
        """
    
    def vector(self,term:str,size:int=0):
        model = "text-embedding-3-small"
        if size > 0:
            model = "text-embedding-3-large"

        response = self.client.embeddings.create(
            model=model,
            input=term,
        )

        return response.data

    def request(self,item:LineBot_Requset)->str:       

        # system prompt setting
        temple = markdownReader("prompts/agent.md")
        system_prompt = temple.substitute(
            time = self.time,
            userid = item.userID
        )

        self.memory.append({"role":"system","content":system_prompt})
        self.memory.append({
                "role":"user",
                "content": item.message,
                "metadata":{
                    "category":"question"
                }
            })

        resp = self.__get_gpt_response()

        msg = resp.choices[0].message
        Tc = msg.tool_calls
        
        # Tool Limit
        # if Tc is None:
        #     print("抱歉，我無法執行你的要求")
        #     return "抱歉，我無法執行你的要求"

        while Tc is not None:
            self.__add_tool_message(Tc,msg)
            self.__gpt_tool_call(Tc)

            resp = self.__get_gpt_response()
            Tc = resp.choices[0].message.tool_calls
            print(resp.choices[0].message.content)
        
        return resp.choices[0].message.content

    def __gpt_tool_call(self,Tc:ChatCompletionMessageFunctionToolCall):
        for tc in Tc:
            name = tc.function.name
            args = json.loads(tc.function.arguments or "{}")
            print(f"{name}:{args}")
            if name in DISPATCH:
                try:
                    result = DISPATCH[name](**args)
                except TypeError as e:
                    result = {"error": f"bad arguments: {e}"}
                except Exception as e:
                    result = {"error": f"handler failed: {e}"}
            else:
                result = {"error": f"unknown tool: {name}"}
                    
            print(result)

            ##回傳function執行結果
            self.memory.append(
                {
                    "role":"tool",
                    "tool_call_id":tc.id,
                    "content":json.dumps(result,ensure_ascii=False),
                    "metadata":{
                        "category":"tool_result"
                    }
                }
            )
        
    def __get_gpt_response(self)->ChatCompletion:
        return self.client.chat.completions.create(
            model=self.defult_model,
            messages=self.memory,
            tools=TOOLS
        )

    def __add_tool_message(self, Tc, msg):
        self.memory.append({
            "role": "assistant",
            "content": msg.content or "",
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    }
                ## 在陣列中append新的json
                } for tc in Tc
            ]
        })
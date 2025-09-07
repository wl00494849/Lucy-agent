from typing import List
from openai import OpenAI
from pydantic import BaseModel
from openai.types.chat import ChatCompletionMessageFunctionToolCall,ChatCompletionMessage,ChatCompletion
from src.dispatch import DISPATCH
from src.tool_dsc import TOOLS
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import os

class LLMs:
    class LineBot_Requset(BaseModel):
        message:str
        userID:str

    def __init__(self,defult_model:str=""):
        self.__api_key = os.getenv("OPENAI_API_KEY")
        self.defult_model = defult_model or "gpt-4.1-mini"
        self.client = OpenAI(api_key=self.__api_key)
        self.memory = []
        self.time = datetime.now(ZoneInfo("Asia/Taipei")).strftime("當地臺北時間:%Y-%m-%d %H:%M:%S")

    def request(self,item:LineBot_Requset)->str:       

        self.memory.append({"role": "system","content": "妳是個可靠的秘書。請以繁體中文回答。"})
        self.memory.append({"role": "system","content": f"LineBot UserID:{item.userID}"})
        self.memory.append({"role": "system","content": self.time})
        self.memory.append({"role": "user","content": item.message})

        resp = self.__get_gpt_response()

        msg = resp.choices[0].message
        Tc = msg.tool_calls

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

            self.memory.append(
                {
                    "role":"tool",
                    "tool_call_id":tc.id,
                    "content":json.dumps(result,ensure_ascii=False)
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
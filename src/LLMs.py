from typing import List
from openai import OpenAI
from pydantic import BaseModel
from openai.types.chat import ChatCompletionMessageFunctionToolCall,ChatCompletionMessage
from src.dispatch import DISPATCH
from src.tool_dsc import TOOLS
import json
import os

class LLMs:
    class GPT_Requset(BaseModel):
        prompt:str

    def __init__(self,defult_model:str=""):
        self.__api_key = os.getenv("OPENAI_API_KEY")
        self.defult_model = defult_model or "gpt-4.1-mini"
        self.client = OpenAI(api_key=self.__api_key)
        self.memory = []

    def request(self,item:GPT_Requset)->str:
        model = self.defult_model             

        self.memory.append({"role": "system","content": "請以繁體中文回答。"})
        self.memory.append({"role": "user","content": item.prompt})

        resp = self.client.chat.completions.create(
            model=model,
            messages=self.memory,
            tools=TOOLS
        )

        msg = resp.choices[0].message

        if (Tc :=  msg.tool_calls) is not None:
            self.__add_tool_message(Tc,msg)
            self.__gpt_tool_call(Tc)

            resp = self.client.chat.completions.create(
                model=model,
                messages=self.memory
            )

            print(resp.choices[0].message.content)
                

        return resp.choices[0].message.content

    def __gpt_tool_call(self,Tc:ChatCompletionMessageFunctionToolCall):
        for tc in Tc:
            name = tc.function.name
            args = json.loads(tc.function.arguments or "{}")
            if name in DISPATCH:
                if name in DISPATCH:
                    try:
                        result = DISPATCH[name](**args)
                    except TypeError as e:
                        result = {"error": f"bad arguments: {e}"}
                    except Exception as e:
                        result = {"error": f"handler failed: {e}"}
                else:
                    result = {"error": f"unknown tool: {name}"}

                self.memory.append(
                    {
                        "role":"tool",
                        "tool_call_id":tc.id,
                        "name":name,
                        "content":json.dumps(result,ensure_ascii=False)
                    }
                )

    def __add_tool_message(self,Tc:ChatCompletionMessageFunctionToolCall,msg:ChatCompletionMessage):
        for tc in Tc:
            self.memory.append({
                "role": "assistant",
                "content":  msg.content or "",
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments,
                        }
                    }]
            })
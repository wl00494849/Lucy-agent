from typing import List
from openai import OpenAI
from pydantic import BaseModel
from openai.types.chat import ChatCompletionMessageFunctionToolCall
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

    def request(self,item:GPT_Requset)->str:
        model = self.defult_model             

        messages = []
        messages.append({"role": "system","content": "請以繁體中文回答。"})
        messages.append({"role": "user","content": item.prompt})

        resp = self.client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS
        )

        msg = resp.choices[0].message

        if (Tc :=  msg.tool_calls) is not None:
            messages.append({
                "role": "assistant",
                "content":  msg.content or "",
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments,  # 字串即可
                    }
                }
            for tc in Tc
            ],
            })

            tool_msg = gpt_tool_call(Tc)

            for msg in tool_msg:
                messages.append(msg)
                resp = self.client.chat.completions.create(
                    model=model,
                    messages=messages
            )

        return resp.choices[0].message.content

def gpt_tool_call(Tc:ChatCompletionMessageFunctionToolCall)->List:
    message = []
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
            message.append(
                {
                    "role":"tool",
                    "tool_call_id":tc.id,
                    "name":name,
                    "content":json.dumps(result,ensure_ascii=False)
                }
            )
    return message
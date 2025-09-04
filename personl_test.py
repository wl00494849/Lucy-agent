from src.env import load_env
from src.LLMs import LLMs

load_env()

while True:
        prompt = input("請輸入問題：")
        gpt = LLMs()
        gpt.request(LLMs.LineBot_Requset(message=prompt,userID=""))
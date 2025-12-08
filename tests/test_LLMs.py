import unittest
from src.env import load_env
from src.LLMs import LLMs

load_env()

class TestMath(unittest.TestCase):

    def test_LLMs(self):
        gpt = LLMs()
        req = LLMs.LineBot_Requset(message="這是測試項目，請只回覆我測試成功",userID="")
        result = gpt.linebot_gpt(req)
        print(result)
        self.assertEqual(result,"測試成功")

    def test_LLMs_tool(self):
        try:
            gpt = LLMs()
            req = LLMs.LineBot_Requset(message="請給我你的系統資訊",userID="")
            gpt.linebot_gpt(req)
        except Exception as e:
            print("Tool fail:",e)

if __name__ == "__main__":
    unittest.main()
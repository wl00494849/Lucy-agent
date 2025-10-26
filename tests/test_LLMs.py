import unittest
from src.env import load_env
from src.LLMs import LLMs

load_env()

class TestMath(unittest.TestCase):
    def test_LLMs(self):
        gpt = LLMs()
        req = LLMs.LineBot_Requset(message="這是測試項目，請只回覆我測試成功",userID="")
        result = gpt.request(req)
        print(result)
        self.assertEqual(result,"測試成功")

if __name__ == "__main__":
    unittest.main()
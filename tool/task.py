from datetime import datetime,timedelta
from zoneinfo import ZoneInfo
import time
import threading
import requests
import os

class Task:
    def __init__(self):
        self.chatbot_url = os.getenv("LINEBOT_API_URL")
        self.time_now = datetime.now(ZoneInfo("Asia/Taipei"))
        self.task_pool = []

    def timer_notify_bySec(self,time_sec:int,message:str,userid:str)->str:
        "LineBot倒數計時通知，以秒數為單位"
        timer = threading.Timer(interval=time_sec,function=self.chatbot_notify,
                                kwargs={
                                    "message":message,
                                    "userid":userid
                                    })
        
        timer.start()
        time_up = self.time_now + timedelta(seconds=time_sec)
        time_up.strftime("%Y-%m-%d %H:%M:%S")

        return f"設定成功{time_up}通知"
    
    def chatbot_notify(self,message:str,userid:str):
        retries = 3
        print(message)
        for attempt in range(1,retries+1):
            try :
                url = self.chatbot_url + "/push_message"
                data = {"message":message,"userID":userid}
                resp = requests.post(url=url,json=data)
                return resp.status_code
            except Exception as e:
                print(e)
                if attempt < retries:
                    time.sleep(5)
                else:
                    return 500
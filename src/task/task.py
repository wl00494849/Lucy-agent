from datetime import datetime,timedelta
import threading
import requests
import os

class TASK:
    def __init__(self):
        self.linebot_url = os.getenv("LINEBOT_API_URL")

    def timer_notify(self,time_sec:int,message:str,userid:str)->str:
        timer = threading.Timer(interval=time_sec,function=self.linebot_notify,
                                kwargs={
                                    "message":message,
                                    "userid":userid
                                    })
        
        timer.start()
        now = datetime.now()
        time_up = now + timedelta(seconds=time_sec)

        time_up.strftime("%Y-%m-%d %H:%M:%S")

        return f"設定成功{time_up}通知"
    
    def linebot_notify(self,message:str,userid:str):
        url = self.linebot_url + "/push_message"
        date = {"message":message,"userID":userid}
        resp = requests.post(url=url,json=date)
        print(resp.status_code)
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo
from dateutil import parser
import threading
import requests
import os

class Task:
    def __init__(self):
        self.linebot_url = os.getenv("LINEBOT_API_URL")
        self.time_now = datetime.now(ZoneInfo("Asia/Taipei"))
        self.task_pool = []

    def timer_notify_byISO8601(self,time_iso:str,message:str,userid:str)->str:
        "LineBot以ISO8601定時通知"
        end_time = parser.isoparse(time_iso)
        diff = end_time - self.time_now
        timer = threading.Timer(interval=diff.total_seconds,function=self.linebot_notify,
                                kwargs={
                                    "message":message,
                                    "userid":userid
                                    })
        
        timer.start()
        end_time.strftime("%Y-%m-%d %H:%M:%S")

        return f"設定成功{end_time}通知"

    def timer_notify_bySec(self,time_sec:int,message:str,userid:str)->str:
        "LineBot倒數計時通知，以秒數為單位"
        timer = threading.Timer(interval=time_sec,function=self.linebot_notify,
                                kwargs={
                                    "message":message,
                                    "userid":userid
                                    })
        
        timer.start()
        time_up = self.time_now + timedelta(seconds=time_sec)
        time_up.strftime("%Y-%m-%d %H:%M:%S")

        return f"設定成功{time_up}通知"
    
    def linebot_notify(self,message:str,userid:str):
        url = self.linebot_url + "/push_message"
        date = {"message":message,"userID":userid}
        resp = requests.post(url=url,json=date)
        print(resp.status_code)
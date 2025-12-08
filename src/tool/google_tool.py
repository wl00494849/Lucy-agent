from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

class Google_Tool:
        
    def __init__(self):
        self.USER_EMAIL = os.getenv("USER_GOOGLE_EMAIL")
        self.GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS") or "credentials.json"
        self.creds = service_account.Credentials.from_service_account_file(
            self.GOOGLE_APPLICATION_CREDENTIALS,
            scopes=["https://www.googleapis.com/auth/calendar"],
        )   
        self.service = build("calendar", "v3", credentials=self.creds)
        
    def __repr__(self):
        return f"""
        Google_Tool(USER_EMAIL = {self.USER_EMAIL})
        """
        
    def create_calendar_event(self,
                              summary: str,
                              start_time: str,
                              end_time: str,
                              remind_time: int = None,
                              description: str = ""
                              )->str:
        try:
            if remind_time is not None:
                reminders = {
                    "useDefault": False,
                    'overrides': [
                            {"method": "popup", "minutes": remind_time},
                        ]
                }
            else:
                reminders = {
                    "useDefault": True
                }

            event_body = {
                "summary": summary,
                "description": description,
                "start": {
                    "dateTime": start_time,
                    "timeZone": "Asia/Taipei",
                },
                "end": {
                    "dateTime": end_time,
                    "timeZone": "Asia/Taipei",
                },
                "reminders": reminders
            }
            created_event = self.service.events().insert(
                calendarId=self.USER_EMAIL,
                body=event_body,
                sendUpdates="all"
            ).execute()

            return f"事件建立成功：{created_event.get('htmlLink')}"
        except Exception as e:
            return f"行事曆建立失敗:{e}"
        
    def get_calendar_list(self,start_time:str,end_time:str):
        try :
            
            events_result = self.service.events().list(
                calendarId = self.USER_EMAIL,
                timeMin = start_time,
                timeMax = end_time,
                singleEvents=True,
                orderBy="startTime"
            ).execute()

            events = events_result.get("items", [])
            li:list[dict] = []

            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                end = event["end"].get("dateTime",event["end"].get("date"))
                li.append({
                            "summary":event["summary"],
                            "start_time":start,
                            "end_time":end
                            })  
            return li
        except Exception as e:
            return f"行事曆清單讀取失敗:{e}"
        
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime,timedelta
import pytz
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
            return e
        
    def get_calendar_list(self)->str:
        try :
            tz = pytz.timezone("Asia/Taipei")
            now = datetime.now(tz=tz)
            start_day = datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=tz)
            end_day = start_day + timedelta(days=1)

            events_result = self.service.events().list(
                calendarId = self.USER_EMAIL,
                timeMin = start_day,
                timeMax = end_day,
                singleEvents=True,
                orderBy="startTime"
            )

            events = events_result.get("items", [])

            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                print(start, event["summary"])
            
        except Exception as e:
            return e
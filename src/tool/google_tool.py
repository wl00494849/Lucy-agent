from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

class Google_Tool:
        
    def __init__(self):
        self.user_email = os.getenv("USER_GOOGLE_EMAIL")
        self.GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self.creds = service_account.Credentials.from_service_account_file(
                self.GOOGLE_APPLICATION_CREDENTIALS,
                scopes=["https://www.googleapis.com/auth/calendar"],
        )
        
    def create_calendar_event(self,
                              summary: str,
                              start_time: str,
                              end_time: str,
                              remind_time: int = None,
                              description: str = ""
                              )->str:
        try:
            service = build("calendar", "v3", credentials=self.creds)
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
            created_event = service.events().insert(
                calendarId=self.user_email,
                body=event_body,
                sendUpdates="all"
            ).execute()

            return f"事件建立成功：{created_event.get('htmlLink')}"
        except Exception as e:
            return e
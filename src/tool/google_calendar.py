import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def create_calendar_event_tool(args: dict):
    print(args)
    creds = service_account.Credentials.from_service_account_file(
        "credentials.json",
        scopes=["https://www.googleapis.com/auth/calendar"],
    )
        
    service = build("calendar", "v3", credentials=creds)

    event = {
        "summary": args["summary"],
        "description": args.get("description"),
        "location": args.get("location"),
        "start": {"dateTime": args["start_datetime"], "timeZone": args.get("timezone","Asia/Taipei")},
        "end": {"dateTime": args["end_datetime"], "timeZone": args.get("timezone","Asia/Taipei")},
        "attendees": [{"email": e} for e in args.get("attendees", [])],
    }

    if isinstance(args.get("reminders_minutes_before"), int):
        event["reminders"] = {
            "useDefault": False,
            "overrides": [{"method": "popup", "minutes": args["reminders_minutes_before"]}],
        }

    created = service.events().insert(calendarId="primary", body=event).execute()
    print(f"事件已建立：{created.get('htmlLink')}")
    return f"事件已建立：{created.get('htmlLink')}"
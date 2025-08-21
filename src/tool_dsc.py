
get_system_information_tool = {
    "type":"function",
    "function":{
        "name":"get_system_information",
        "description":"取得系統資訊",
        "parameters":{},
        "required":[]
    }
}

get_taipei_time_tool = {
    "type":"function",
    "function":{
        "name":"get_taipei_time",
        "description":"取得當地時間(臺北)",
        "parameters":{},
        "required":[]
    }
}

create_calendar_event_tool = {
        "type": "function",
        "function": {
            "name": "create_calendar_event",
            "description": "在 Google 行事曆建立事件(ISO 8601 時間）。",
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"},
                    "description": {"type": "string"},
                    "location": {"type": "string"},
                    "start_datetime": {"type": "string"},
                    "end_datetime": {"type": "string"},
                    "timezone": {"type": "string", "default": "Asia/Taipei"},
                    "attendees": {
                        "type": "array",
                        "items": {"type": "string", "format": "email"},
                    },
                    "reminders_minutes_before": {"type": "integer"},
                },
                "required": ["summary", "start_datetime", "end_datetime"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
TOOLS = [get_system_information_tool,get_taipei_time_tool]
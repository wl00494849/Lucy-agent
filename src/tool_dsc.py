timer_notify_byISO8601 = {
    "type":"function",
    "function":{
        "name":"timer_notify_byISO8601",
        "description":"LineBot長時間定時通知",
        "parameters":{
            "type":"object",
            "properties": {
                "time_iso":{"type":"string","description": "ISO8601時間格式，通知時間"},
                "message":{"type":"string","description":"時間到通知訊息"},
                "userid":{"type":"string","description":"LineBot的UserID"}
            }
        },
        "required":["time_iso","message","userid"]
    }
}

timer_notify_bySec = {
    "type":"function",
    "function":{
        "name":"timer_notify_bySec",
        "description":"LineBot短時間倒數計時通知",
        "parameters":{
            "type":"object",
            "properties": {
                "time_sec":{"type":"integer","description": "倒數秒數，例如 60 代表 1 分鐘後通知"},
                "message":{"type":"string","description":"時間到通知訊息"},
                "userid":{"type":"string","description":"LineBot的UserID"}
            }
        },
        "required":["time_sec","message","userid"]
    }
}

get_system_information_tool = {
    "type":"function",
    "function":{
        "name":"get_system_information",
        "description":"取得系統資訊",
        "parameters":{},
        "required":[]
    }
}

# get_taipei_time_tool = {
#     "type":"function",
#     "function":{
#         "name":"get_taipei_time",
#         "description":"取得當地時間(臺北)",
#         "parameters":{},
#         "required":[]
#     }
# }

create_calendar_event_tool = {
  "type": "function",
  "function": {
    "name": "create_calendar_event",
    "description": "在 Google 行事曆建立事件（時間需為 ISO 8601，含時區）。",
    "parameters": {
      "type": "object",
      "description": "建立行事曆事件所需的參數物件。",
      "properties": {
        "summary": {
          "type": "string",
          "description": "事件標題"
        },
        "description": {
          "type": "string",
          "description": "事件描述"
        },
        "start_time": {
          "type": "string",
          "description": "開始時間（ISO 8601，含時區）"
        },
        "end_time": {
          "type": "string",
          "description": "結束時間（ISO 8601，含時區）"
        },
        "remind_time": {
          "type": "integer",
          "description": "幾分鐘前跳出通知（popup）"
        }
      },
      "required": ["summary","start_time","end_time"],
    }
  }
}

TOOLS = [get_system_information_tool,timer_notify_bySec,create_calendar_event_tool]
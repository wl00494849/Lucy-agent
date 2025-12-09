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

get_system_config_tool = {
    "type":"function",
    "function":{
        "name":"get_system_config",
        "description":"取得系統設定",
        "parameters":{},
        "required":[]
    }
}


create_calendar_event_tool = {
  "type": "function",
  "function": {
    "name": "create_calendar_event",
    "description": "在 Google 行事曆建立事件（時間需為 ISO 8601，含時區)。",
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

get_calendar_list_tool = {
    "type":"function",
    "function":{
        "name":"get_calendar_list",
        "description":"取得行事曆清單（時間為ISO 8601，含時區）",
        "parameters":{
          "type": "object",
          "description": "建立行事曆事件所需的參數物件。",
          "properties": {
              "start_time":{
                "type": "string",
                "description": "開始時間（ISO 8601，含時區）"
              },
              "end_time":{
                "type": "string",
                "description": "結束時間（ISO 8601，含時區）"
              }
          }
        },
        "required":[]
    }
}

rag = {
    "name":"rag",
    "description":"根據使用者問題從知識庫中檢索最相關的內容。當問題需要外部文件、技術資料、FAQ、產品規格、公司政策或任何非模型內知識時，使用此工具。",
    "parameters": {
    "type": "object",
    "properties": {
      "question": {
          "type": "string",
          "description": "使用者的查詢內容，例如：'如何重設密碼？'"
        }
      }
    },
    "required": ["question"]
}

TOOLS = [
          get_system_information_tool,
          timer_notify_bySec,
          create_calendar_event_tool,
          get_calendar_list_tool,
          get_system_config_tool,
          rag
        ]

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
TOOLS = [get_system_information_tool,get_taipei_time_tool]
import platform
import json

class Sys_Tool:

    def get_system_information()->str:
        return f"""
        系統名稱:{platform.system()}
        系統平台:{platform.platform()}
        處理器:{platform.processor()}
        """
 
    def get_system_config()->str:
        with open("config.json","r", encoding="utf-8") as f:
            config = json.load(f)
        return f"""
        是否自動提醒：{config["auto_reminder"]}
        提醒時間：{config["reminder_time"]}
        """
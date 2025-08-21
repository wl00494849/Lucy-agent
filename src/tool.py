import platform
from datetime import datetime
from zoneinfo import ZoneInfo

class TOOL:
    def get_system_information()->str:
        "取得當前系統資訊"
        return f"""
        系統名稱:{platform.system()}
        系統平台:{platform.platform()}
        處理器:{platform.processor()}
        """
    def get_taipei_time()->str:
        "取得當地時間(臺北)"
        now = datetime.now(ZoneInfo("Asia/Taipei"))
        time = now.strftime("Taipei Time:%Y-%m-%d %H:%M:%S")
        return time
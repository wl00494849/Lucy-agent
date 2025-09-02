import platform

class Sys_Tool:

    def get_system_information()->str:
        "取得當前系統資訊"
        return f"""
        系統名稱:{platform.system()}
        系統平台:{platform.platform()}
        處理器:{platform.processor()}
        """
 
    
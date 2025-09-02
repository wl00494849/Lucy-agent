from src.tool.sys_tool import Sys_Tool
from src.tool.google_tool import Google_Tool
from src.task.task import Task

Task = Task()
Google_Tool = Google_Tool()

DISPATCH = {
    "get_system_information":Sys_Tool.get_system_information,
    "timer_notify_bySec":Task.timer_notify_bySec,
    "timer_notify_byISO8601":Task.timer_notify_byISO8601,
    "create_calendar_event":Google_Tool.create_calendar_event
    # "get_taipei_time":SYS_TOOL.get_taipei_time,
}
from src.tool.sys_tool import SYS_TOOL
from src.tool.google_calendar import create_calendar_event_tool
from src.task.task import TASK

TASK = TASK()

DISPATCH = {
    "get_system_information":SYS_TOOL.get_system_information,
    "timer_notify_bySec":TASK.timer_notify_bySec,
    "timer_notify_byISO8601":TASK.timer_notify_byISO8601,
    "create_calendar_event_tool":create_calendar_event_tool
    # "get_taipei_time":SYS_TOOL.get_taipei_time,
}
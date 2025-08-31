from src.tool.sys_tool import SYS_TOOL
from src.tool.google_tool import google_tool
from src.task.task import TASK

TASK = TASK()
GOOGLE_TOOL = google_tool()

DISPATCH = {
    "get_system_information":SYS_TOOL.get_system_information,
    "timer_notify_bySec":TASK.timer_notify_bySec,
    "timer_notify_byISO8601":TASK.timer_notify_byISO8601,
    "create_calendar_event":GOOGLE_TOOL.create_calendar_event
    # "get_taipei_time":SYS_TOOL.get_taipei_time,
}
from src.tool.sys_tool import SYS_TOOL
from src.task.task import TASK

TASK = TASK()

DISPATCH = {
    "get_system_information":SYS_TOOL.get_system_information,
    "timer_notify_bySec":TASK.timer_notify_bySec,
    "timer_notify_byISO8601":TASK.timer_notify_byISO8601
    # "get_taipei_time":SYS_TOOL.get_taipei_time,
}
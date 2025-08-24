from src.tool.sys_tool import SYS_TOOL
from src.task.task import TASK

TASK = TASK()

DISPATCH = {
    "get_system_information":SYS_TOOL.get_system_information,
    "get_taipei_time":SYS_TOOL.get_taipei_time,
    "timer_notify":TASK.timer_notify
}
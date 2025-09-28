from src.tool.sys_tool import Sys_Tool
from src.tool.google_tool import Google_Tool
from src.task.task import Task
from src.env import load_env

load_env()

Task = Task()
Google_Tool = Google_Tool()

DISPATCH = {
    "get_system_information":Sys_Tool.get_system_information,
    "get_system_config":Sys_Tool.get_system_config,
    "timer_notify_bySec":Task.timer_notify_bySec,
    "create_calendar_event":Google_Tool.create_calendar_event,
    "get_calendar_list":Google_Tool.get_calendar_list
}
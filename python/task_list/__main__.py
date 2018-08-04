import sys

from python.task_list.console import Console
from python.task_list.task_list import TaskList

task_list = TaskList(Console(sys.stdin, sys.stdout))
task_list.run()

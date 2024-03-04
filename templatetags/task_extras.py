from django import template
from typing import TypedDict

register = template.Library()


class Task(TypedDict):
    title: str
    status: str


@register.simple_tag()
def get_tasks_by_status(tasks: list[Task], status: str) -> list[Task]: 
    return [task for task in tasks if task['status']==status]
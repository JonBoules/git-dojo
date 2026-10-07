"""A tiny in-memory to-do list. Practice material for the git-dojo exercises."""

from dataclasses import dataclass

import os

@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    priority: str = "normal"

PRIORITIES = ("low", "normal", "high")

class TodoList:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(self, title: str, priority: str = "normal") -> Task:
        if not title.strip():
            raise ValueError("title must not be empty")
        if priority not in PRIORITIES:
            raise ValueError(f"priority must be one of {PRIORITIES}")
        task = Task(id=len(self._tasks) + 1, title=title.strip(), priority=priority)
        self._tasks.append(task)
        return task

    def complete_task(self, task_id: int) -> Task:
        task = self._tasks[task_id]
        task.done = True
        return task

    def list_tasks(self) -> list[Task]:
        return list(self._tasks)

    def clear_completed(self) -> int:
        remaining = [task for task in self._tasks if not task.done]
        removed = len(self._tasks) - len(remaining)
        self._tasks = remaining
        return removed

def format_task(task: Task) -> str:
    return f"{task.id}. {task.title}"

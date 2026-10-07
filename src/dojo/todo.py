"""A tiny in-memory to-do list. Practice material for the git-dojo exercises."""

from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    priority: str = "high"


class TodoList:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(self, title: str) -> Task:
        if not title.strip():
            raise ValueError("title must not be empty")
        task = Task(id=len(self._tasks) + 1, title=title.strip())
        self._tasks.append(task)
        return task

    def complete_task(self, task_id: int) -> Task:
        task = self._tasks[task_id]
        task.done = True
        return task

    def list_tasks(self) -> list[Task]:
        return list(self._tasks)


def format_task(task: Task) -> str:
    return f"{task.id}. {task.title}"

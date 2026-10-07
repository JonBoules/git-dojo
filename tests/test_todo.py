import pytest

from dojo.todo import TodoList, format_task


def test_add_task_assigns_incrementing_ids():
    todo = TodoList()
    first = todo.add_task("Buy milk")
    second = todo.add_task("Walk dog")
    assert (first.id, second.id) == (1, 2)


def test_add_task_strips_whitespace():
    assert TodoList().add_task("  Buy milk  ").title == "Buy milk"


def test_add_task_rejects_empty_title():
    with pytest.raises(ValueError):
        TodoList().add_task("   ")


def test_list_tasks_returns_copy():
    todo = TodoList()
    todo.add_task("A")
    todo.list_tasks().clear()
    assert len(todo.list_tasks()) == 1


def test_format_task():
    task = TodoList().add_task("Buy milk")
    assert format_task(task) == "1. Buy milk"

def test_add_task_default_priority_is_normal():
    assert TodoList().add_task("Buy milk").priority == "normal"


def test_add_task_accepts_explicit_priority():
    assert TodoList().add_task("Buy milk", priority="high").priority == "high"


def test_add_task_rejects_invalid_priority():
    with pytest.raises(ValueError):
        TodoList().add_task("Buy milk", priority="urgent")
        
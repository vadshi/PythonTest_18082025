from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field

import pytest


@dataclass
class Task:
    summary: str | None = "usual task"  # change None as default value
    owner: str | None = "user"  # change None as default value
    state: str = "todo"
    id: int | None = field(default=None, compare=False) # change compare value to True

    @classmethod
    def from_dict(cls, d):
        return Task(**d)
    def to_dict(self):
        return asdict(self)
    

def test_field_access():
    task = Task("important task", "petr", "todo", 123)
    assert task.summary == "important task"
    assert task.owner == "petr"
    assert task.state == "todo"
    assert task.id == 123

@pytest.mark.skip(reason="Change defaults values and now it's disabled")
def test_defaults():
    task = Task()
    assert task.summary is None
    assert task.owner is None
    assert task.state == "todo"
    assert task.id is None


def test_equility():
    task1 = Task("important task", "petr", "todo", 123)
    task2 = Task("important task", "petr", "todo", 123)
    assert task1 == task2


def test_equility_with_diff_ids():
    task1 = Task("important task", "petr", "todo", 123)
    task2 = Task("important task", "petr", "todo", 467)
    assert task1 == task2


def test_inequility():
    task1 = Task("important task", "petr", "todo", 123)
    task2 = Task("unimportant task", "petr", "todo", 123)
    assert task1 != task2


def test_task_from_dict():
    task1 = Task("important task", "petr", "todo", 123)
    task2_dict = {
        "summary": "important task",
        "owner": "petr", 
        "state": "todo",
        "id": 123,
    }
    task2 = Task.from_dict(task2_dict)
    assert task1 == task2


def test_task_to_dict():
    task1 = Task("important task", "petr", "todo", 123)
    task2_dict = task1.to_dict()
    task2_expected = {
        "summary": "important task",
        "owner": "petr", 
        "state": "todo",
        "id": 123,
    }
    assert task2_dict == task2_expected
"""
API for the tasks project
"""
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field

from .db import DB

__all__ = [
    "Task",
    "TasksDB",
    "TasksException",
    "MissingSummary",
    "InvalidTaskId",
]


@dataclass
class Task:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        return Task(**d)
    def to_dict(self):
        return asdict(self)


class TasksException(Exception):
    pass


class MissingSummary(TasksException):
    pass


class InvalidTaskId(TasksException):
    pass


class TasksDB:
    def __init__(self, db_path):
        self._db_path = db_path
        self._db = DB(db_path, "tasks_db")

    def add_task(self, task: Task) -> int:
        """Add a task, return the id of task."""
        if not task.summary:
            raise MissingSummary
        if task.owner is None:
            task.owner = ""
        id = self._db.create(task.to_dict())
        self._db.update(id, {"id": id})
        return id

    def get_task(self, task_id: int) -> Task:
        """Return a task with a matching id."""
        db_item = self._db.read(task_id)
        if db_item is not None:
            return Task.from_dict(db_item)
        else:
            raise InvalidTaskId(task_id)

    def list_tasks(self, owner=None, state=None):
        """Return a list of tasks."""
        all = self._db.read_all()
        if (owner is not None) and (state is not None):
            return [
                Task.from_dict(t)
                for t in all
                if (t["owner"] == owner and t["state"] == state)
            ]
        elif owner is not None:
            return [
                Task.from_dict(t) for t in all if t["owner"] == owner
            ]
        elif state is not None:
            return [
                Task.from_dict(t) for t in all if t["state"] == state
            ]
        else:
            return [Task.from_dict(t) for t in all]

    def count(self) -> int:
        """Return the number of tasks in db."""
        return self._db.count()

    def update_task(self, task_id: int, task_mods: Task) -> None:
        """Update a task with modifications."""
        try:
            self._db.update(task_id, task_mods.to_dict())
        except KeyError as exc:
            raise InvalidTaskId(task_id) from exc

    def start(self, task_id: int):
        """Set a task state to 'in prog'."""
        self.update_task(task_id, Task(state="in prog"))

    def finish(self, task_id: int):
        """Set a task state to 'done'."""
        self.update_task(task_id, Task(state="done"))

    def delete_task(self, task_id: int) -> None:
        """Remove a task from db with given task_id."""
        try:
            self._db.delete(task_id)
        except KeyError as exc:
            raise InvalidTaskId(task_id) from exc

    def delete_all(self) -> None:
        """Remove all tasks from db."""
        self._db.delete_all()

    def close(self):
        self._db.close()

    def path(self):
        return self._db_path

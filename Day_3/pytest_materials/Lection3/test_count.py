import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import tasks


@pytest.fixture()
def tasks_db():
    # ===== это setup =====
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = tasks.TasksDB(db_path)
        yield db
        # ===== это teardown =====
        db.close()


def test_empty(tasks_db):
    assert tasks_db.count() == 0


def test_two(tasks_db):
    tasks_db.add_task(tasks.Task("first task added via fixture"))
    tasks_db.add_task(tasks.Task("second task added via fixture"))
    assert tasks_db.count() == 2
# subdir1/conftest.py
from pathlib import Path
from tempfile import TemporaryDirectory
import tasks
import pytest


@pytest.fixture(scope="session")
def tasks_db():
    """TasksDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = tasks.TasksDB(db_path)
        yield db
        db.close()
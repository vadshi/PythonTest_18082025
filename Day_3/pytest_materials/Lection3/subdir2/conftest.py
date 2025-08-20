# subdir2/conftest.py
from pathlib import Path
from tempfile import TemporaryDirectory
import tasks
import pytest


@pytest.fixture(scope="session")
def db():
    """TasksDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = tasks.TasksDB(db_path)
        yield db_
        db_.close()


@pytest.fixture(scope="function")
def tasks_db(db):
    """TasksDB object that's empty"""
    db.delete_all()
    return db

"""Command Line Interface (CLI) for tasks project."""
import os
from io import StringIO
import pathlib
import rich
from rich.table import Table # type: ignore
from contextlib import contextmanager
from typing import List

import tasks

import typer

app = typer.Typer(add_completion=False)


@app.command()
def version():
    """Return version of tasks application"""
    print(tasks.__version__)


@app.command()
def add(
    summary: List[str], owner: str = typer.Option(None, "-o", "--owner")
):
    """Add a task to db."""
    summary = " ".join(summary) if summary else None
    with tasks_db() as db:
        db.add_task(tasks.Task(summary, owner, state="todo"))


@app.command()
def delete(task_id: int):
    """Remove task in db with given id."""
    with tasks_db() as db:
        try:
            db.delete_task(task_id)
        except tasks.InvalidTaskId:
            print(f"Error: Invalid task id {task_id}")


@app.command("list")
def list_tasks(
    owner: str = typer.Option(None, "-o", "--owner"),
    state: str = typer.Option(None, "-s", "--state"),
):
    """
    List tasks in db.
    """
    with tasks_db() as db:
        the_tasks = db.list_tasks(owner=owner, state=state)
        table = Table(box=rich.box.SIMPLE) # type: ignore
        table.add_column("ID")
        table.add_column("state")
        table.add_column("owner")
        table.add_column("summary")
        for t in the_tasks:
            owner = "" if t.owner is None else t.owner
            table.add_row(str(t.id), t.state, owner, t.summary)
        out = StringIO()
        rich.print(table, file=out)
        print(out.getvalue())


@app.command()
def update(
    task_id: int,
    owner: str = typer.Option(None, "-o", "--owner"),
    summary: List[str] = typer.Option(None, "-s", "--summary"),
):
    """Modify a task in db with given id with new info."""
    summary = " ".join(summary) if summary else None
    with tasks_db() as db:
        try:
            db.update_task(
                task_id, tasks.Task(summary, owner, state=None)
            )
        except tasks.InvalidTaskId:
            print(f"Error: Invalid task id {task_id}")


@app.command()
def start(task_id: int):
    """Set a task state to 'in prog'."""
    with tasks_db() as db:
        try:
            db.start(task_id)
        except tasks.InvalidTaskId:
            print(f"Error: Invalid task id {task_id}")


@app.command()
def finish(task_id: int):
    """Set a task state to 'done'."""
    with tasks_db() as db:
        try:
            db.finish(task_id)
        except tasks.InvalidTaskId:
            print(f"Error: Invalid task id {task_id}")


@app.command()
def config():
    """List the path to the Tasks db."""
    with tasks_db() as db:
        print(db.path())


@app.command()
def count():
    """Return number of tasks in db."""
    with tasks_db() as db:
        print(db.count())


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Tasks is a small command line task tracking application.
    """
    if ctx.invoked_subcommand is None:
        list_tasks(owner=None, state=None)


def get_path():
    db_path_env = os.getenv("TASKS_DB_DIR", "")
    if db_path_env:
        db_path = pathlib.Path(db_path_env)
    else:
        db_path = pathlib.Path.home() / "tasks_store"
    return db_path


@contextmanager
def tasks_db():
    db_path = get_path()
    db = tasks.TasksDB(db_path)
    yield db
    db.close()

from tasks import Task


def test_field_access():
    task = Task("important task", "petr", "todo", 123)
    assert task.summary == "important task"
    assert task.owner == "petr"
    assert task.state == "todo"
    assert task.id == 123


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

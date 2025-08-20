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
import tasks


def test_empty(tasks_db):
    assert tasks_db.count() == 0


def test_two(tasks_db):
    tasks_db.add_task(tasks.Task("first"))
    tasks_db.add_task(tasks.Task("second"))
    assert tasks_db.count() == 2
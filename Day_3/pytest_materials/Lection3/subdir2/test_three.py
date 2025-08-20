import tasks

def test_three(tasks_db):
    tasks_db.add_task(tasks.Task("first"))
    tasks_db.add_task(tasks.Task("second"))
    tasks_db.add_task(tasks.Task("third"))
    assert tasks_db.count() == 3
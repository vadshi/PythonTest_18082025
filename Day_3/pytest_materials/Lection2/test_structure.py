from tasks import Task


def test_task_to_dict():
    # GIVEN a Task object with known contents
    task1 = Task("important task", "petr", "todo", 123)

    # WHEN we call method .to_dict on the object
    task2_dict = task1.to_dict()

    # THEN the result will be a dictionary with known contents    
    task2_expected = {
        "summary": "important task",
        "owner": "petr", 
        "state": "todo",
        "id": 123,
    }
    assert task2_dict == task2_expected
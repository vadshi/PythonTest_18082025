import tasks
import pytest


def test_no_path_raises():
    with pytest.raises(TypeError):
        tasks.TasksDB() # type: ignore


def test_raises_with_info():
    match_regex = "missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regex):
        tasks.TasksDB() # type: ignore


def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:
        tasks.TasksDB() # type: ignore
    expected = "missing 1 required positional argument"
    assert expected in str(exc_info)
# test_rename_fixture.py
import pytest
from collections import namedtuple

@pytest.fixture(name="ultimate_answer")
def ultimate_answer_fixture():
    return 42


def test_everything(ultimate_answer):
    print("I want show this message")
    assert ultimate_answer == 42


def test_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured[0].rstrip() == "hello"

def test_output2():
    User = namedtuple("User", ["name", "age"])
    user1 = User("petr", 20)
    assert type(user1) is User
    print(f'{user1.name = }')
    print(f'{user1.age = }')
    print("Repeat")
    print(f'{user1[0] = }')
    print(f'{user1[1] = }')

import pytest

# мы запускаем pytest --setup-show test_fixtures.py, чтобы посмотреть порядок вызовов
# фикстуры вызываются перед каждым тестом (кроме тех, у которых scope="module")


@pytest.fixture()
def sample_list():
    # простой список; эту фикстуру используем в двух тестах
    return [1, 2, 3]


@pytest.fixture()
def sample_dict():
    """Простой словарь для pytest --fixtures"""
    return {"name": "Alice", "age": 20}


@pytest.fixture(scope="module")
def sample_tuple():
    # scope="module": фикстура выполняется один раз на модуль, а не на каждый тест
    print("setup")   # имитация подготовки ресурса
    yield (1, 2)     # я сделал так, потому что это проще
    print("teardown")  # имитация очистки ресурса


def test_list_len(sample_list):
    # фикстура вызывается перед каждым тестом (function scope)
    assert len(sample_list) == 3


def test_list_content(sample_list):
    # второй тест использует ту же фикстуру
    assert sample_list[0] == 1


def test_dict_value(sample_dict):
    assert sample_dict["name"] == "Alice"


def test_tuple_content(sample_tuple):
    assert sample_tuple == (1, 2)
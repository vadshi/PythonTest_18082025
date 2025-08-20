## Фикстуры (pytest fixtures)

`Фикстуры (fixtures)` - вспомогательные тестовые функции, которые необходимы для структурирования тестового кода практически любой сложной программы. Фикстуры — это функции, которые pytest запускает до (а иногда и после) выполнения самих тестовых функций.  

Код в фикстуре может выполнять любые ваши задачи. Вы можете использовать фикстуры для получения набора данных, на котором будут работать тесты. Вы можете использовать фикстуры для приведения системы в известное состояние перед запуском теста. Фикстуры также используются для подготовки данных для нескольких тестов.

### Знакомство с фикстурами
1. Создайте файл `test_fixtures.py`
```python
import pytest

@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42
```

### Setup и teardown

Фикстуры очень помогут нам в тестировании приложения Tasks. Приложение Tasks разработано с API, которое берёт на себя большую часть работы и логики, и с простым CLI. Учитывая, что пользовательский интерфейс довольно слабо использует логику, сосредоточение большей части тестирования на API даст нам максимальную отдачу от вложенных средств. Приложение Tasks также использует базу данных, и работа с ней — это как раз то, где фикстуры окажутся очень полезны.


Для примеры создадим файл `test_count_initial.py`
```python
from pathlib import Path
from tempfile import TemporaryDirectory
import tasks


def test_empty():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = tasks.TasksDB(db_path)
        
        count = db.count()
        db.close()

        assert count == 0
```
Тестовая функция перегружена, поэтому разделим ее на инициализацию базы и тест:

```python
import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import tasks


@pytest.fixture()
def tasks_db():
    # ===== это setup =====
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = tasks.TasksDB(db_path)
        yield db
        # ===== это teardown =====
        db.close()


def test_empty(tasks_db):
    assert tasks_db.count() == 0
```

Сразу видно, что сама тестовая функция стала гораздо проще для чтения, поскольку мы перенесли всю инициализацию базы данных в фикстуру `tasks_db`.

### Детализация запуска фикстуры в тестовой функции
Запустим тестовую функцию с параметром `--setup-show`:
```
pytest --setup-show test_count.py
```
Буква `F` указывает на `function scope` т.е. область видимости в рамках функции.
Это значит, что фикстура будет запускаться перед началом каждой тестовой функции и завершаться после ее отработки.

`function scope` это область видимости по умолчанию(by default), но при работе с БД мы хотели бы установить соединение один раз и потом уже пользоваться этим соединением, а не делать это каждый раз для каждой тестовой функции.

На помощь приходит параметр `scope`, который мы должны указать в фикстуре, например так:
```python
@pytest.fixture(scope="module")
def tasks_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = tasks.TasksDB(db_path)
        yield db
        db.close()
```

Запустим тест еще раз и увидим разницу.


### Различные области видимости фикстур

`scope='function'`  

    Выполняется один раз для каждой тестовой функции. Раздел настройки(setup) выполняется перед каждым тестом, использующим фикстуру. Раздел завершения(teardown) выполняется после каждого теста, использующего фикстуру. Это область действия по умолчанию, если параметр области действия не указан.  

`scope='class'`  

    Выполняется один раз для каждого тестового класса, независимо от количества тестовых методов в классе.  

`scope='module'`  

    Выполняется один раз для каждого модуля, независимо от количества тестовых функций, методов или других фикстур в модуле, использующих его.  

`scope='package'`  

    Выполняется один раз для каждого пакета или каталога тестов, независимо от количества тестовых функций, методов или других фикстур в пакете, использующих его.  

`scope='session'` 

    Выполняется один раз для каждого сеанса. Все тестовые методы и функции, использующие фикстуру, области действия сеанса используют один общий вызов настройки и завершения.


Если фикстура определена в тестовом модуле, области действия сеанса и пакета действуют
так же, как область действия модуля. Чтобы использовать эти дополнительные области действия, нам нужно
поместить их в файл `conftest.py`.


### Файл conftest.py и scope='session'

1. Создайте отдельную директорию и в ней два файла `conftest.py` и `test_count.py`
```python
# subdir/conftest.py
from pathlib import Path
from tempfile import TemporaryDirectory
import tasks
import pytest


@pytest.fixture(scope="session")
def tasks_db():
    """TasksDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = tasks.TasksDB(db_path)
        yield db
        db.close()
```

```python
# subdir/test_count.py
import tasks


def test_empty(tasks_db):
    assert tasks_db.count() == 0


def test_two(tasks_db):
    tasks_db.add_task(tasks.Task("first"))
    tasks_db.add_task(tasks.Task("second"))
    assert tasks_db.count() == 2
```
Запустите pytest и посмотрите на scope
```
cd subdir
pytest --setup-show test_count.py
```

*ВАЖНОЕ ЗАМЕЧАНИЕ!!!*  
Хотя `conftest.py` — это модуль Python, его не следует импортировать в тестовые файлы. Файл conftest.py автоматически считывается pytest, поэтому вам не нужно импортировать conftest явно где либо.

### Расположение фикстур
Чтобы понять где расположена фикстура, которую мы используем в тестовом файле, нужно использовать соответствующи ключи:
```
pytest --fixtures -v
```
При выводе мы увидим встроенные фикстуры и фикстуру из файла `conftest.py`

Можно узнать какая фикстура используется конкретным тестом:
```
pytest --fixtures-per-test test_count.py::test_empty
```

### Незавимость от порядка выполнения

Существует проверенное временем правило, согласно которому тесты не должны зависеть от порядка выполнения. И, очевидно, в данном случае это так. `test_three` проходит отлично, если мы запускаем его отдельно, но выдаёт ошибку, если он запускается после `test_two`.

Чтобы решить эту задачу, изменим нашу фикстура, разделив ее на две:
```python
# subdir/conftest.py
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
```
Скопируйте в новую директорию файлы `test_count.py` и `test_three.py` и посмотрите как это работает:
```
pytest --setup-show
```

### Параметр `name` для переименования фикстур

Имя фикстуры, указанное в списке параметров тестов и других фикстур, использующих её, обычно совпадает с именем функции этой фикстуры. Однако pytest позволяет переименовывать фикстуры с помощью параметра `name` в `@pytest.fixture()`:
```python
# test_rename_fixture.py
import pytest


@pytest.fixture(name="ultimate_answer")
def ultimate_answer_fixture():
    return 42


def test_everything(ultimate_answer):
    assert ultimate_answer == 42
```

Обычно переименование используется только для тех фикстур, которые находятся в том же модуле, что и тесты, использующие их, поскольку переименование фикстуры может затруднить поиск её определения. Однако помните, что всегда есть параметр `--fixtures`, который поможет вам найти местоположение фикстуры.
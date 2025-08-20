import pytest

@pytest.fixture()
def number_list():
    """Список чисел"""
    return [1, 2, 3, 4, 5]

@pytest.fixture()
def user_data():
    """Словарь с данными пользователя"""
    return {
        'name': 'Ольга Потуй',
        'age': 30,
        'email': 'op@example.com',
        'is_active': True
    }

@pytest.fixture()
def product_info():
    """Кортеж с инфо о продукте"""
    print("\nСоздание фикстуры product_info добавив (scope='module')")
    return ("Ноутбук", "Apple MacBook Pro", 2023, 1999.99) 

@pytest.fixture(scope='module')
def product_info_2():
    """Фикстура 2 возвращает кортеж с информацией о продукте"""
    print("\n Начало работы фикстуры product_info_2")
    product_data = ("Ноутбук", "Apple MacBook Pro", 2023, 1999.99)
    print(f"Данные продукта: {product_data}")
    yield product_data
    print("Фикстура product_info_2 завершила работ!")

@pytest.fixture()
def sample_text():
    """Фикстура возвращает строку текста"""
    return "Hello, pytest fixtures!"

def test_number_list_length(number_list):
    """Тест проверяет длину списка из фикстуры"""
    assert len(number_list) == 5
    assert isinstance(number_list, list)

def test_number_list_content(number_list):
    """Тест проверяет содержимое списка из фикстуры"""
    assert number_list[0] == 1
    assert number_list[-1] == 5
    assert sum(number_list) == 15

def test_user_data_structure(user_data):
    """Тест проверяет структуру данных пользователя"""
    assert 'name' in user_data
    assert 'age' in user_data
    assert 'email' in user_data
    assert user_data['is_active'] is True

def test_user_data_values(user_data):
    """Тест проверяет значения в данных пользователя"""
    assert isinstance(user_data['name'], str)
    assert user_data['age'] >= 18 
    assert '@' in user_data['email'] 

def test_product_info_values(product_info):
    """Тест проверяет значения информации о продукте"""
    assert isinstance(product_info[0], str) 
    assert isinstance(product_info[1], str) 
    assert isinstance(product_info[2], int)  # Год - целое число
    assert isinstance(product_info[3], float)  # Цена - число с плавающей точкой
    
    assert product_info[2] >= 2000  # Год выпуска не раньше 2000
    assert product_info[3] > 0  # Цена не отрицательная

def test_product_info_structure(product_info_2):
    """Проверяем структуру информации о продукте"""
    print(f"Тест 1 выполняется с product_info: {product_info_2}")
    assert len(product_info_2) == 4
    assert isinstance(product_info_2, tuple)
    assert product_info_2[0] == "Ноутбук"
    assert product_info_2[1] == "Apple MacBook Pro"
    print("Тест 1 завершен")

def test_sample_text_length(sample_text):
    """Проверяем длину текста"""
    assert len(sample_text) > 0
    assert isinstance(sample_text, str)

def test_sample_text_content(sample_text):
    """Проверяем содержание текста"""
    assert "pytest" in sample_text.lower()
    assert sample_text.startswith("Hello")

def test_multiple_fixtures(number_list, user_data, sample_text):
    """Тест использует несколько фикстур одновременно"""
    # список
    assert len(number_list) == 5
    
    # Проверяем словарь
    assert user_data['name'] == 'Ольга Потуй'
    
    # Проверяем текст
    assert "fixtures" in sample_text
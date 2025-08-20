"""
Задача №1
1.1 Написать программу, которая расшифрует строку.
Каждая символ - это две цифры. Отчет с 00 -> 'a', 01 -> 'b' и до 25 -> 'z',
26 - это пробел, он не входит в набор букв
Вход: строка из цифр. Выход: Текст.

1.2 Реализовать и расшифровку и зашифровку через функции
In/Out: ‘070411111426152419071413’ <-> Out/In: ‘hello python’

1.3 Добавить обработку неправильных входных данных.

1.4 Написать тесты для отработки корректных и некорректных данных.

"""
import string as st


def create_dict(key="chars"):
    letters = st.ascii_lowercase + ' '
    if key == 'digits':
        result = {f"{index:02}": value for index, value in enumerate(letters)}
    else:
        result = {value: f"{index:02}" for index, value in enumerate(letters)}
    return result


def decode(s: str) -> str:
    """ Decode digits string and return letters string"""
    assert s.isdigit()
    digits: dict = create_dict(key="digits")
    pairs = [one + two for one, two in zip(s[::2], s[1::2], strict=True)]
    try:
        result = ''.join(digits[pair] for pair in pairs)
    except KeyError as ke:
        raise ValueError("Bad chars in string")
    else:
        return result


def encode(s: str) -> str:
    """ Encode chars string and return digits string"""
    chars: dict = create_dict()
    return ''.join(chars[symbol] for symbol in s)


def main():
    """Основная функция для тестирования"""
    # Тестовый пример
    test_encrypted = '070411111426152419071413'
    test_decrypted = 'hello python'
    
    print("Тестирование:")
    print(f"Зашифрованный текст: {test_encrypted}")
    print(f"Расшифрованный текст: {decode(test_encrypted)}")
    print(f"Обратное шифрование: {encode(test_decrypted)}")
    print(f"Совпадение: {encode(test_decrypted) == test_encrypted}")
    
    # Интерактивный режим
    print("\n" + "="*50)
    print("Интерактивный режим:")
    
    while True:
        print("\nВыберите действие:")
        print("1 - Расшифровать")
        print("2 - Зашифровать")
        print("0 - Выход")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            try:
                encrypted = input("Введите зашифрованный текст: ").strip()
                decrypted = decode(encrypted)
                print(f"Результат: '{decrypted}'")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == '2':
            try:
                text = input("Введите текст для шифрования: ").strip()
                encrypted = encode(text)
                print(f"Результат: {encrypted}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
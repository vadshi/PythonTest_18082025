def decrypt(encrypted_text):
    """
    Расшифровывает строку, зашифрованную по правилу:
    Каждые 2 цифры -> символ: 00='a', 01='b', ..., 25='z', 26=' '
    """
    if not encrypted_text:
        return ""
    
    # Проверка на четность длины
    if len(encrypted_text) % 2:
        raise ValueError("Неправильный формат входных данных: длина должна быть четной")
    
    # Проверка, что все символы - цифры
    if not encrypted_text.isdigit():
        raise ValueError("Неправильный формат входных данных: должны быть только цифры")
    
    result = []
    
    for i in range(0, len(encrypted_text), 2):
        # Берем две цифры
        code_str = encrypted_text[i:i+2]
        code = int(code_str)
        
        # Проверка диапазона
        if code < 0 or code > 26:
            raise ValueError(f"Неправильный код: {code_str}. Допустимые значения: 00-26")
        
        # Преобразуем код в символ
        if code == 26:
            result.append(' ')
        else:
            result.append(chr(ord('a') + code))
    
    return ''.join(result)


def encrypt(text):
    """
    Шифрует строку по правилу:
    'a'->00, 'b'->01, ..., 'z'->25, ' '->26
    """
    if not text:
        return ""
    
    result = []
    
    for char in text:
        if char == ' ':
            result.append('26')
        elif 'a' <= char <= 'z':
            code = ord(char) - ord('a')
            result.append(f"{code:02d}")  # Форматируем как двузначное число
        else:
            raise ValueError(f"Неподдерживаемый символ: '{char}'. "
                           f"Допустимы только строчные буквы a-z и пробел")
    
    return ''.join(result)


def main():
    """Основная функция для тестирования"""
    # Тестовый пример
    test_encrypted = '070411111426152419071413'
    test_decrypted = 'hello python'
    
    print("Тестирование:")
    print(f"Зашифрованный текст: {test_encrypted}")
    print(f"Расшифрованный текст: {decrypt(test_encrypted)}")
    print(f"Обратное шифрование: {encrypt(test_decrypted)}")
    print(f"Совпадение: {encrypt(test_decrypted) == test_encrypted}")
    
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
                decrypted = decrypt(encrypted)
                print(f"Результат: '{decrypted}'")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == '2':
            try:
                text = input("Введите текст для шифрования: ").strip()
                encrypted = encrypt(text)
                print(f"Результат: {encrypted}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
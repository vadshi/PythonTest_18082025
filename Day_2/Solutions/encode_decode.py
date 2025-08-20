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

def get_chars_w_digits(key: str = 'char') -> dict:
    ''' Counts chars with digits '''
    result = {}
    for digit in range(0, 26):
        char = st.ascii_lowercase[digit]
        str_digit = str(digit) if len(str(digit)) == 2 else f'0{digit}'
        if key == 'digit':
            result[str_digit] = char
            continue
        result[char] = str_digit
    if key == 'digit':
        result['26'] = ' '
    result[' '] = '26'
    return result

def encode(string: str) -> str:
    ''' Encode string to digits'''
    if not isinstance(string, str):
        raise TypeError(f'need str you give {type(string)}')
    char_dict = get_chars_w_digits()
    result = ''
    for char in string:
        if char not in st.ascii_lowercase + ' ':
            raise ValueError('invalid symbol in string')
        result += char_dict[char] 
    return result

print(encode('hello python'))


def decode(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError(f'need str you give {type(string)}')
    if len(string) / 2 != round(len(string) / 2, 0):
        raise ValueError('string value must be divisible by 2')
    digit_dict = get_chars_w_digits(key='digit')
    step_slice = 0
    result = ''
    for slice in range(2, len(string)+1, 2):
        number = string[step_slice:slice]
        step_slice = slice
        char = digit_dict.get(number)
        if not char:
            raise ValueError('invalid digit in string')
        result += char
    return result

print(decode('070411111426152419071413'))




'''
Задача №1
Вход:
Пользователь должен ввести 'правильный' пароль, состоящий из:
цифр, букв латинского алфавита(строчные и прописные) и
специальных символов  special = '_!@#$%^&'.
Всего 4 набора различных символов.
В пароле обязательно должен быть хотя бы один символ из каждого набора.
Длина пароля от 8(мин) до 15(макс) символов включительно.
Максимальное количество попыток ввода неправильного пароля - 5.
Каждый раз выводим номер попытки.
Желательно выводить пояснение, почему пароль не принят и
что нужно исправить.

* Добавить проверку, что в пароле только символы из 4-х наборов.

Как вариант:
check_password('some string') -> tuple[bool, str]
(True, reasons)
(False, reasons)


Оформить решения в виде модуля

import string as st
st.digits
st.ascii_lowercase
st.ascii_uppercase
special = '_!@#$%^&'

Выход:
пароль подходит / не подходит

Пример:
пароль подходит -> o58anuahaunH!
пароль подходит -> aaaAAA111!!!
пароль не подходит -> saucacAusacu8
'''


import string as st


def check_password(password: str) -> tuple[bool, str]:
    """ check password strong or not"""
    plen = len(password)
    if plen > 15 or plen < 8:
        plen_text = 'low'
        if plen > 15:
            plen_text = 'high'
        return False, f'password {plen_text} len'
    
    result = ''
    special_symbols = '_!@#$%^&'
    lower = upper = digit = special = False
    for p in password:
        if p in st.digits:
            digit = True
        elif p in st.ascii_lowercase:
            lower = True
        elif p in st.ascii_uppercase:
            upper = True
        elif p in special_symbols:
            special = True
        else:
            return False, f'in password wrong char'

    
    if not lower:
        result += 'lowercase not in password\n'
    if not upper:
        result += 'uppercase not in password\n'
    if not digit:
        result += 'digits not in password\n'
    if not special:
        result += 'special not in password'
        
    
    if result:
        return False, result
    return True, result
    

# res = check_password('o58anuahaunH!')
# print(res)
# res = check_password('aaaAAA111!!!')
# print(res)
# res = check_password('saucacAusacu8')
# print(res)
# res = check_password('saucacusacu8')
# print(res)
# res = check_password('12')
# print(res)
# res = check_password('12ффваыфвыфвщ')
# print(res)


def user_input():
    for ipt in range(1, 6):
        password = input(f'try {ipt} - write password: ')
        status, msg = check_password(password)
        if status:
            print('password correct')
            break
        print(f'password incorrect: {msg}')
    else:
        print("All attepmts have finished")


if __name__ == "__main__":
    user_input()
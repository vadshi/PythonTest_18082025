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

special = '_!@#$%^&'
_allowed = set(st.digits + st.ascii_lowercase + st.ascii_uppercase + special)


def check_password(pwd):
    """
    Проверка пароля по правилам задачи.

    Возвращает:
        (True, "пароль подходит") или (False, "пояснение что исправить")
    """
    reasons = []

    # 1) Длина
    if len(pwd) < 8:
        reasons.append("длина меньше 8 символов")
    if len(pwd) > 15:
        reasons.append("длина больше 15 символов")

    # 2) Наличие обязательных типов символов
    # if not any(ch in st.digits for ch in pwd):
    if not set(pwd) & set(st.digits):
        reasons.append("добавьте хотя бы одну цифру")
    if not any(ch in st.ascii_lowercase for ch in pwd):
        reasons.append("добавьте хотя бы одну строчную латинскую букву")
    if not any(ch in st.ascii_uppercase for ch in pwd):
        reasons.append("добавьте хотя бы одну прописную (заглавную) латинскую букву")
    if not any(ch in special for ch in pwd):
        reasons.append(f"добавьте хотя бы один спецсимвол из набора: {special}")

    # 3) Только разрешённые символы
    invalid = set(pwd) - _allowed
    if invalid:
        # Выводим уникальные запрещённые символы для наглядности
        uniq = "".join(sorted(invalid))
        reasons.append(f"обнаружены запрещённые символы: {uniq!r}")

    if reasons:
        return (False, reasons)
    return (True, "пароль подходит")


def main():
    max_tries = 5
    for attempt in range(1, max_tries + 1):
        pwd = input(f"Попытка {attempt}/{max_tries}. Введите пароль: ")
        ok, msg = check_password(pwd)
        if ok:
            print(f"Пароль подходит -> {pwd}")
            return
        else:
            print("Пароль не подходит:", *msg, sep='\n')

    print("Превышено число попыток. Доступ запрещён.")


if __name__ == "__main__":
    main()
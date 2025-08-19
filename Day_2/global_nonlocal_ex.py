# Пример класа-декоратора
# from functools import total_ordering
# from pprint import pprint

s1 = 'hello'
s2 = 'python'
a = 4
b = 8.4

# 4 области видимости LEGB (Local, Enclosed, Global, Builtin)

# pprint(globals()) # Словарь всех глобальных переменных

def func_one():
    a = 99
    b = 22 # свободная переменная
    # pprint(locals()) # Словарь всех локальных переменных  
    # print(a)
    # a += 1 # a = a + 1
    def inner_func():
        nonlocal a       
        print(f'{locals() = }')
        a = 2 + b
        return a
    return inner_func



# res = func_one()

# print(f'{a = }')
# print(type(res))
# print(res())

# Пример декоратора
def rub_to_usd(function_as_param):
    def wrapper(*args, **kwargs):
        # print(f'{locals() = }')
        result = function_as_param(*args, **kwargs)
        new_result = float(result[:-3]) / 93
        return f"{new_result:.2f} EUR"
    return wrapper


@rub_to_usd  # func_sum = rub_to_usd(func_sum)
def func_sum(price, count):
    """ Return data format: <float> RUB"""
    return f"{price * count * 1.18} RUB"

print(func_sum(100, 10))
print(func_sum)

# Использование функции-декоратора без синтаксического сахара
# func_sum_usd = rub_to_usd(func_sum)
# print(func_sum_usd(100, 10))

# Было
# my_func = lambda x: x ** 2 + 3 * x + 100 

# Стало
def my_func(x: int) -> int:
    return x ** 2 + 3 * x + 100


print(my_func(1))
# print(my_func("100")) # error
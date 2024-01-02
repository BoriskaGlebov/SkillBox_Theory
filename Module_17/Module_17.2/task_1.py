from typing import Callable
import inspect
import types
import builtins


# count = 0


def counter(func: Callable) -> Callable:
    count = 0

    def wrap_func(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Функция {func.__name__} вызвана {count} раз')
        return func(*args, **kwargs)

    return wrap_func


# @counter
def hello() -> None:
    print('Привет товарищи')


print('Задача 1. Счётчик 2')
# print(isinstance(hello, types.FunctionType))
rez = hello()
# hello()
# hello()
# hello()
# print(f'Первый элемент списка = {dir('task_1.py')[1]}')
# print(f'Вытащил атрибут с таким названием= {getattr('task_1.py', dir('task_1.py')[1])}')
# print(f'Тип этого атрибута = {type(getattr('task_1.py', dir('task_1.py')[0]))}')
# print(f'Проверяю метод он или нет = {isinstance(getattr('task_1.py', dir('task_1.py')[0]), Callable)}')


# for name, data in inspect.:
#     if name.startswith('__'):
#         continue
#     print(name, end=' ')
print(dir('task_1.py'))
print(dir('__buildin__'))
print(dir('task_1.py')==dir('__buildin__'))
from typing import Callable
import time


def timer(funk: Callable) -> int:
    """
    Считает вермя выполнения программы
    :return: время
    """""
    start = time.time()
    rez = funk()
    end = time.time()
    rez_time = end - start
    print(f'Программа работала {rez_time} секунд')
    return rez


def generator() -> int:
    """"Генерирурирует список и находит его сумму"""""
    gen_sum = sum([el for el in range(100000)])
    return gen_sum


print('Задача 2. Таймер')

tim = timer(generator)
print(tim)
print(type(tim))

from typing import Callable
import time


def timer(funk: Callable) -> Callable:
    def wrapper_funk():
        start = time.time()
        rez = funk()
        end = time.time()
        rez_time = end - start
        print(f'Программа работала {rez_time} секунд')
        return rez

    return wrapper_funk


@timer
def generator() -> int:
    gen_rez = sum([el * 123 for el in range(5000000)])
    return gen_rez


print('Задача 2. Таймер')

tim = generator()
print(tim)

import functools
import time
from datetime import datetime
from typing import Callable


def create_time(cls):
    @functools.wraps(cls)
    def wrapper(*args):
        instance = cls(*args)
        print('Время создания объекта', datetime.now())
        # print(dir(cls))
        return instance

    return wrapper


def timer(func: Callable):
    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        start = time.time()
        rez = func(*args)
        end = time.time()
        print(f'Время работы функции {end - start}')
        return rez

    return wrapper


def decorator_for_metods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for i_metod in dir(cls):
            if i_metod.startswith('__') is False:
                cur_metod = getattr(cls, i_metod)
                decorated_metod = decorator(cur_metod)
                setattr(cls, i_metod, decorated_metod)
        return cls

    return decorate



@create_time
@decorator_for_metods(timer)
class Function:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([el ** 2 for el in range(self.max_num)])
        return result

    def cubes_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([el ** 3 for el in range(self.max_num)])
        return result


print('Задача 1. Create time')
first1 = Function(10000)
time.sleep(1)
print(first1.squares_sum())
print(first1.cubes_sum())

first2 = Function(20000)
time.sleep(1)
first3 = Function(30000)


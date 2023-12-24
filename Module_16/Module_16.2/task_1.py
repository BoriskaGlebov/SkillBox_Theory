import time
from contextlib import contextmanager
from collections.abc import Iterator


def generator() -> int:
    """"Генерирует список и находит его сумму"""""
    gen_sum = sum([el for el in range(10000000)])
    return gen_sum


@contextmanager
def timer() -> Iterator:
    start = time.time()
    yield
    print(time.time() - start)


print('Задача 1. Таймер')

with timer() as t1:
    print(generator())

with timer() as t2:
    print(generator())

with timer() as t3:
    print(generator())

from time import sleep
from typing import Callable, Any


def do_n(_funk=None, *, n: int = 1) -> Callable:
    def twice(funk: Callable) -> Any:
        def wrap_funk() -> None:
            for _ in range(3):
                sleep(n)
                print(funk())
            return

        return wrap_funk

    if _funk is None:
        return twice
    else:
        return twice(_funk)


@do_n(n=3)
def generator() -> int:
    """"Генерирует список и находит его сумму"""""
    gen_sum = sum([el for el in range(100)])
    return gen_sum


@do_n
def generator2() -> int:
    """"Генерирует список и находит его сумму"""""
    gen_sum = sum([el * 4 for el in range(100)])
    return gen_sum


print('Задача 2. Замедление кода 2')
print(generator())
print(generator2())

from typing import Callable, Any


def do_n(n):
    def twice(func: Callable) -> Any:
        def wrap_funk():
            for _ in range(n):
                print(func())
            return

        return wrap_funk

    return twice


@do_n(3)
def generator() -> int:
    """"Генерирует список и находит его сумму"""""
    gen_sum = sum([el for el in range(1000000)])
    return gen_sum


print('Задача 1. Повторение кода')

print(generator())

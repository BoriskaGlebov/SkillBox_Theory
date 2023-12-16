from typing import Callable, Any

print('Задача 1. Функции')


def funk_1(x: int) -> Any:
    """
    Функция возвращает сумму числа с 10
    
    :return int
    """""
    return x + 10


def funk_2(funk: Callable, num: int) -> int:
    """Выводит перемноженный результат"""""
    rez = funk(num) ** 2
    return rez


d = funk_2(funk_1, 9)
print(type(d))
c = d()

from typing import Callable, Any

print('Задача 1. Двойной вызов')


def decorator(funk: Callable) -> Callable:
    """Функция декоратор"""""

    def wrapper_funk(*args) -> Any:
        rez = funk(*args) + funk(*args)
        return rez

    return wrapper_funk

@decorator
def greeting(name: str) -> str:
    return f'Привет, {name}!'


d = greeting('tom')
print(d)

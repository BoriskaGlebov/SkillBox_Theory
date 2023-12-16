from typing import Callable

print('Задача 2. Плагины')
plugins = {}


def get_plugins(funk: Callable):
    plugins[funk] = funk
    return funk


@get_plugins
def hello(name):
    print(f'Hello {name}')


@get_plugins
def good(name):
    print(f'Good {name} ')


print(plugins)
d = hello('Tom')
c = good('mike')

from typing import Callable

print('Задача 1. Сэндвич')


def get_some_salad(func):
    def wrap_that_salad(*args, **kwargs):
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")

    return wrap_that_salad


def get_some_buns(func):
    def wrap_that_buns(*args, **kwargs):
        print("</----------\\>")
        func(*args, **kwargs)
        print("<\\______/>")

    return wrap_that_buns


@get_some_buns
@get_some_salad
def filling_burger(filler):
    print(filler)


filling_burger("ветчина")
# d = ingredients('помидоры', 'ветчина', 'салат')

import random

print('Задача 3. Универсальная программа')


def func(object_1):
    if isinstance(object_1, dict):
        object_1 = object_1.values()
    list_out = [val for ind, val in enumerate(object_1) if ind % 2 == 0]
    return list_out


tuple_1 = (100, 200, 300, 'буква', 0, 2, 'а')
str_1 = 'О Дивный Новый мир!'
list_1 = [100, 200, 300, 'буква', 0, 2, 'а']
dict_1 = dict(enumerate([chr(random.randint(ord('А'), ord('я'))) for _ in range(10)]))
print(tuple_1)
print(str_1)
print(list_1)
print(dict_1)
print()
print(func(tuple_1))
print(func(str_1))
print(func(list_1))
print(func(dict_1))


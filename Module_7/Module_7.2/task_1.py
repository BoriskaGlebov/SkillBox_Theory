import random

print('Задача 1. Создание кортежей')

tuplу_1 = tuple([random.randint(0, 5) for _ in range(10)])
print(tuplу_1)
tuplу_2 = tuple([random.randint(-5, 0) for _ in range(10)])
print(tuplу_2)
print(tuplу_1 + tuplу_2)
print((tuplу_1+tuplу_2).count(0))

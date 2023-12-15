print('Задача 1. Список чётных чисел')
import random

a = 1
b = 26
print(f'a= {a} b= {b}')

list_1 = [x for x in range(a, b + 1) if x % 2 == 0]
list_2 = [(x if x % 2 == 0 else x**3 ) for x in range(a, b + 1)]
print(list_1)
print(list_2)

print('Задача 2. Семинар')
import random
nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

print('Исходный список nums_1: ', nums_1)
print('Исходный список nums_2: ', nums_2)
print()

set_1 = set(nums_1)
set_2 = set(nums_2)

print('Исходное множетсво nums_1: ', set_1)
print('Исходное множество nums_2: ', set_2)
print()
set_1.remove(min(set_1))
set_2.remove(min(set_2))
print('Удаляю минимальное число из nums_1: ', set_1)
print('Удаляю минимальное число из nums_2: ', set_2)
print()
rnd_1 = random.randint(100,200)
rnd_2 = random.randint(100,200)
print('Рандомное сло от 100 до 200:', rnd_1, rnd_2 )
set_1.add(rnd_1)
set_2.add(rnd_2)
print('Добавил рандомное число в nums_1: ', set_1)
print('Добавил рандомное число в nums_2: ', set_2)
print()
print('Объединение множеств: ', set_1.union(set_2))
print('Общие элементы  множеств: ', set_1.intersection(set_2))
print('Элементы, входящие в nums_2, но не входящие в nums_1:', set_2.difference(set_1))



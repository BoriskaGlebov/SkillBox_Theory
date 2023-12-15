import random
print('Задача 2. Словари из списков')

list_1 = [chr(random.randint(ord('А'), ord('я'))) for _ in range(10)]
print(list_1)
list_2 = [chr(random.randint(ord('А'), ord('я'))) for _ in range(10)]
print(list_2)


print(dict(enumerate(list_1)))
list_2 = dict(enumerate(list_2))
print(list_2)


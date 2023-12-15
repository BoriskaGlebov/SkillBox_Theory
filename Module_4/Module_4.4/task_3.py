print('Задача 3. Удаление части')
import random

list_1 = [random.randint(1, 100) for _ in range(10)]
# A = random.randint(0, 8)
# B = random.randint(A, 9)
A = 5
B = 9
print(list_1)
print(A, B)
list_1[A:B+1] = []
print(list_1)
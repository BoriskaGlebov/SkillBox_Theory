print('Задача 3. Отряды')
import random

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
print('Урон 1 отряда: ', squad_1)
print('Урон 2 отряда: ', squad_2)

squad_3_rez = [('Погиб' if squad_1[el] + squad_2[el] > 100 else 'Выжил')
               for el in range(10)]
print('Состояние третьего отряда: ', squad_3_rez)
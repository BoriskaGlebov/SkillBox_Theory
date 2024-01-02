print('Задача 1. Однострочный код')
user_num = (input('Введите числа: ')).split()
rez = sorted(list(map(int, user_num)))
print(rez)

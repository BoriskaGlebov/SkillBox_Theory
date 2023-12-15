print('Задача 1. Словарь квадратов чисел')

nume = int(input('Введите целое число: '))
square_dict = {}
for i in range(1, nume + 1):
    square_dict[i] = i ** 2
print(square_dict)
for i_info in square_dict:
    print(i_info, '-', square_dict[i_info])

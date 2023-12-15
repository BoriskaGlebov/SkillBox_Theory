print('Задача 2. Кратность')

number = int(input('Кол-во чисел в списке: '))
num_list = []
sum_ind = 0

for ind in range(number):
    in_list = int(input(f'Введите {ind + 1} число: '))
    num_list.append(in_list)
print(num_list)

divider = int(input('Введите делитель: '))

for ind in range(len(num_list)):
    if num_list[ind] % divider == 0:
        print(f'Индекс числа {num_list[ind]}: {ind}')
        sum_ind += ind
print(f'Сумма индексов: {sum_ind}')

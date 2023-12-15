def add_num(num, f_list=None):
    f_list = f_list or []
    f_list.append(num)
    print(f_list)


print('Задача 2. Накопление значений')

add_num(5, [1, 2, 3])
add_num(10)
add_num(15)

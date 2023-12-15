print('Задача 2. Вредоносное ПО')
first_mes = input('Первое сообщение: ')
second_mes = input('Второе сообщение: ')
first_symb = first_mes.count('?') + first_mes.count('!')
sec_symb = second_mes.count('?') + second_mes.count('!')
if first_symb > sec_symb:
    new_mes = first_mes+second_mes
    print(new_mes)
elif first_symb < sec_symb:
    new_mes = second_mes + first_mes
    print(new_mes)
else:
    print('ОЙ!!!')



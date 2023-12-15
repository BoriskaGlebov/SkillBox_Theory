print('Задача 2. Сообщение')
user_str = input('Введите строку: ')
u_symbol = input('Введите дополнительный символ: ')
doble_str_list = [elem * 2 for elem in user_str]
el_str_list = [elem + u_symbol for elem in doble_str_list]
print('Список удвоенных символов:', doble_str_list)
print('Склейка с дополнительным символом: ', el_str_list)

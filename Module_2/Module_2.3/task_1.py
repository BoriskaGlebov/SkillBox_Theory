print('Задача 1. Текстовый редактор: возвращение')
user_str = input('Введите текст для проверки: ')
new_str = ''
count = 0
print(user_str)
# user_list = list(user_str)
# print(user_list)
for ind, symbol in enumerate(user_str):
    if symbol == ':':
        symbol = ';'
        count += 1
    new_str += symbol
print(new_str)
print(count)

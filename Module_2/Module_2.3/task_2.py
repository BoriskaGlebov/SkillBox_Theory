print('Задача 2. Соседи')
user_str = input('Введите строку для проверки: ')
position = int(input('Введите номер символа для поиска соседних: '))
count = 0
user_list = list(user_str)
print('Сосед слева:', user_list[position - 2])
print('Сосед справа:', user_list[position])
for i in user_list:
    if i == user_list[position - 1]:
        count += 1
if count > 1:
    print(f'Таких же символов {count - 1}')
else:
    print('Таких символов нет')

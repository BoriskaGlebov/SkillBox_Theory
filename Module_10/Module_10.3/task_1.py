print('Задача 1. Простая программа')

user_str = input('Введи строку: ')
try:
    user_file = open('input.txt', 'w')
    user_file.write(int(user_str))
except ValueError:
    print('ошибка типа данных')
else:
    print('Без ошибок')
finally:
    user_file.close()
    print(user_file.closed)

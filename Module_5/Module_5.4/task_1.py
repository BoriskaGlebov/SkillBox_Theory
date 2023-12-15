print('Задача 1. Шифр Цезаря 2')
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
user_str = input('Введите строку для шифрования: ').lower()
K = int(input('Введите на сколько сдвинуть: '))
new_list = [alphabet[(alphabet.index(el) + K) % len(alphabet)] if el != ' ' else ' ' for el in user_str]
print(''.join(new_list))

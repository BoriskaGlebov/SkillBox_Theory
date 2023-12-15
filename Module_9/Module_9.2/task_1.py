import os

print('Задача 1. Иконки')

file_name = 'task_1.py'
file_path = os.path.abspath(os.path.join(file_name))
print('Путь\n' + file_path)
if os.path.exists(file_path):
    print('Это Файл')
    print('Размер файла: ', os.path.getsize(file_name), 'байт')
else:
    print('Указанного пути не существует')

import os


def file_finder(path, file_name):
    # print('Веду поиск в папке', path)
    for i_elem in os.listdir(path):
        path_1 = os.path.abspath(os.path.join(path, i_elem))
        if file_name == i_elem:
            print('\t', path_1)
        if os.path.isdir(path_1):
            file_finder(path_1, file_name)
    return


print('Задача 2. Поиск файла')

file_name = 'task_1.py'
# file_path = os.path.abspath(os.path.join('..', '..', '..', 'SkillBox_Theory'))
file_path = os.path.abspath(os.path.join('..', '..'))
print('Ищем файл:', file_name)
print('Ищем в:', file_path)
print()
print('Найдены следующие пути:')
file_finder(file_path, file_name)

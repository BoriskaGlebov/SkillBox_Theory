print('Задача 2. Поиск файла 2')

import os, random


def file_finder(path, file_name):
    file_finder_list = []
    # print('Веду поиск в папке', path)
    for i_elem in os.listdir(path):
        path_1 = os.path.abspath(os.path.join(path, i_elem))
        if file_name == i_elem:
            file_finder_list.append(path_1)
        elif os.path.isdir(path_1):
            rezult = file_finder(path_1, file_name)
            file_finder_list.extend(rezult)
            # if rezult:
            #     file_finder_list.extend(rezult)
    return file_finder_list


print('Задача 2. Поиск файла')

file_name = 'task_1.py'
# file_path = os.path.abspath(os.path.join('..', '..', '..', 'SkillBox_Theory'))
file_path = os.path.abspath(os.path.join('..', '..'))
print('Ищем файл:', file_name)
print('Ищем в:', file_path)
print()
print('Найдены следующие пути:')
print(file_finder(file_path, file_name))
# all_path = file_finder(file_path, file_name)
# num = random.randint(0, len(all_path))
# print(all_path[num])

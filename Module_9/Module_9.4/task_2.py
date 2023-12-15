import os


def finder(path, file_name):
    path_list = []
    for el in os.listdir(path):
        if el == file_name:
            path_list.append(os.path.join(path, el))
            return path_list
        if os.path.isdir(os.path.join(path, el)):
            rez = finder(os.path.join(path, el), file_name)
            path_list.extend(rez)
    return path_list




print('Задача 2. Всё в одном')

path_file = os.path.abspath(os.path.join('..', '..', '..', 'Python_Basic'))
file_name = 'main.py'
print(f'Ищу файл, {file_name} в {path_file}')

rez_path_list = finder(path_file, file_name)
print(rez_path_list[0])


input_file = open('scripts.txt', 'a')
for i_elem in rez_path_list:
    file = open(i_elem, 'r', encoding='utf-8')
    line = ''
    for i_line in file:
        line += i_line
    line += '\n'+(40*'*'+'\n')
    input_file.write(line)
input_file.close()


import os

print('Задача 1. Результаты')
path_1 = os.path.abspath(os.path.join(os.sep, 'task_1', 'group_1.txt'))
path_2 = os.path.abspath(os.path.join(os.sep, 'task_1', 'Additional_info', 'group_2.txt'))
print(path_1)
print(path_2)

file_1 = open(path_1, 'r', encoding='utf-8')
file_2 = open(path_2, 'r', encoding='utf-8')

summa = 0
diff = 0
compose = 1

for i_line in file_1:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])
file_1.close()

for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])

print(summa)
print(diff)
print(compose)

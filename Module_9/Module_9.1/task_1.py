import os

print('Задача 1. Сисадмин')
project_folder = 'access'
project_name = 'admin.bat'

print('Абсолютный путь до файла', os.path.abspath(os.path.join(project_folder, project_name)))
print('Относительный путь до файла', os.path.join(project_folder,project_name))



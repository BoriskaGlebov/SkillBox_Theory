import os

print('Задача 2. Содержимое')

folder_name = 'SkillBox_Theory'
path_to_folder = os.path.abspath(os.path.join('..', '..', '..', folder_name))
print(path_to_folder)
for i_elem in os.listdir(path_to_folder):
    print(os.path.join(path_to_folder,i_elem))

print()
for i_elem in os.listdir(os.path.sep):
    print(i_elem)

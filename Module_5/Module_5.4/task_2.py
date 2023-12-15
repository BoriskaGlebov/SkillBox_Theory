print('Задача 2. Путь к файлу')

addres = 'C:/user/docs/folder/new_file.txt'
print(addres)
disk = input('На каком диске должен лежать файл: ')
value = input('Требуемое расширение файла: ')
value = ''.join(['.', value])
if not addres.startswith(disk):
    print('Диск указон неверно')
if not addres.endswith(value):
    print('неверное расширение файла')
else:
    print('Верно')


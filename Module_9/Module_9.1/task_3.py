import os

print('Задача 3. Корень диска')

print(os.path.join('sd', 'asd', 'asd'))
print(os.path.abspath('sad'))
print(os.path.abspath(os.path.join(os.sep,'sdff')))


print("Корень диска:", os.path.abspath(os.sep))
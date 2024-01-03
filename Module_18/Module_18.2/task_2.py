import re

print('Задача 2. Экранирование спецсимволов')
user_txt = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
print(user_txt)
print(re.findall(r'\\wwood\+\?,', user_txt))

print('Задача 1. Саботаж!')

user_str = 'so~mec~od~e'
print('Ответ:', end='')
for ind, letter in enumerate(user_str):
    if letter == '~':
        print(ind, end=' ')

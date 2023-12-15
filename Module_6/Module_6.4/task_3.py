print('Задача 3. Различные цифры')

user_text = 'ab1n32kz2'
num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
print(user_text)
user_set = set(user_text)
print('Различные цифры строки:', ''.join(user_set.intersection(num_set)))

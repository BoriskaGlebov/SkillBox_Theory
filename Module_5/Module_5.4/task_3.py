print('Задача 3. Удаление части')

# input_str = input('Введите строку: ')
# input_str = 'ПитоН - этО хорошО'
input_str = 'ПиТоН - ЭтО УДоБнО'
lower = len([letter for letter in input_str if letter.islower()])
upper = len([letter for letter in input_str if letter.isupper()])
if lower > upper:
    print(input_str.lower())
else:
    print(input_str.upper())

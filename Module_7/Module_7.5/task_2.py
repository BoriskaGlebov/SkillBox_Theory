print('Задача 2. Контакты 2')
phone_book_dict = {}
while True:
    user_input = input('Введите ФИ - телефон человека: ').split()
    if user_input == []:
        break
    if tuple(user_input[0:2]) not in phone_book_dict.keys():
        phone_book_dict[tuple(user_input[0:2])] = int(user_input[-1])
    else:
        print('Такой контакт уже есть в книге')
    print(phone_book_dict)

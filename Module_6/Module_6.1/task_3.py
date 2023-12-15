print('Задача 3. Контакты')
contacts = {}
while True:
    if contacts:
        for name in contacts:
            print(name, '-', contacts[name])
    else:
        print('<Пусто>')
    info_contact = input('Введите имя и номер контакта: ').split()
    if info_contact == []:
        break
    elif info_contact[0] in contacts:
        print('Ошибка: такое имя уже существует.')
        continue
    elif len(info_contact) != 2:
        print('Ошибка: не указали имя или телефон.')
        continue

    contacts[info_contact[0]] = int(info_contact[1])

print('\n\nТелефонный справочник:')
for name in contacts:
    print(name, '-', contacts[name])

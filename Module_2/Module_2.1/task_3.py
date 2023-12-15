print('Задача 3. Контроль')

num_of_employees = int(input('Кол-во сотрудников в офисе: '))
id_list = []

for id in range(1, num_of_employees + 1):
    id_employees = int(input('ID сотрудника: '))
    id_list.append(id_employees)
print(id_list)

while True:
    id_check = int(input('Какой ID ищем? '))
    for check in id_list:
        if check == id_check:
            print('Сотрудник работает!')
            break
    else:
        print('Сотрудник не работает!')





print('Задача 2. Сокращения')
num_workers = int(input('Кол-во сотрудников: '))
salary = []

for num in range(num_workers):
    new_salary = int(input(f'Зарплата {num + 1} сотрудника: '))
    if new_salary > 0:
        salary.append(new_salary)
print('Осталось сотрудников: ', len(salary))
print('Зарплата:', salary)
print('Максимальная зп: ', max(salary))
print('Минимальная зп: ', min(salary))




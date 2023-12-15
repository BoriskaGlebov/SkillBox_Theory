print('Задача 1. Задачи компаний')
main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

print(main)
main.extend(first_company)
main.extend(second_company)
main.extend(third_company)
print(main)
print('Количество невыполненных задач:', main.count(0))
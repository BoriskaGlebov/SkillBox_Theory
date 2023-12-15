print('Задача 3. Разделители символов')
template = input('введите поздравление({name} {age}): ')
while '{name}' and '{age}' not in template:
    print('Соблюдай формат!')
    template = input('введите поздравление({name} {age}): ')
print(template)
name_list = input('введи ФИ именинника через , : ').split(', ')

age = input('Введи возраст через пробел: ')
age_list = [int(age) for age in age.split()]

for ind in range(len(name_list)):
    print(template.format(name=name_list[ind], age=age_list[ind]))
people = [' '.join([name_list[ind], str(age_list[ind])]) for ind in range(len(name_list))]
print('Именинники: ', ', '.join(people))
# print('Именинники: {0} {1}, '
#       '{0} {1}, '
#       '{0} {1}'.format(
#     name_list, age_list)
# )

print('Задача 1. Имена')


sum = 0

try:
    people_file = open('people.txt', 'r')
    for i_line in people_file:
        if len(i_line.rstrip('\n'))<3:
            raise Exception("Длина строки меньше 3 символов")
        sum += len(i_line.rstrip('\n'))
    print(sum)
except Exception:
    print("Длина строки меньше 3 символов")
finally:
    people_file.close()
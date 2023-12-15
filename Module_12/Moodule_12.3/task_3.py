from random import randint


class MyOwnException(Exception):
    def __str__(self):
        return print('Сам написал ошибку')




print('Задача 3. Кастомные исключения')
with open('numbers.txt', 'w+') as numbers_file:
    for _ in range(10):
        numbers_file.write(f'{str(randint(-1, 5))} {str(randint(-1, 5))} \n')
    numbers_file.seek(0)
    for i_line in numbers_file:
        a, b = i_line.rstrip().split()
        print(a, b)
        try:
            if a >= b:
                c = int(a) / int(b)
                print(c)
            else:
                raise MyOwnException()
        except (ValueError, ZeroDivisionError, MyOwnException) as exc:
            print(f'{exc} {type(exc)} {a},{b}')
            # if isinstance(exc, MyOwnException):
            #     # print(('Нельзя делить большее на меньшее'))
            #     # MyOwnException()
            #     2
            # else:
            #     print(f'{exc} {type(exc)} {a},{b}')

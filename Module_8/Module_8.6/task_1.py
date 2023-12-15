def funk(question, mistake = 'РОт ЗАнят?', attempt=2):
    while attempt != 0:
        attempt -= 1
        us_input = input(question).lower()
        if us_input == 'да':
            return 'Пидр'
        elif us_input == 'нет':
            return 'НеПидр'
        print(mistake)

    else:
        return 'НУ значит не определился'


print('Задача 1. Работа с файлом')


print(funk('ты пидр?', attempt=4))

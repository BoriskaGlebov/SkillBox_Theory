print('Задача 1. Пятый элемент')
BRUCE_WILLIS = 42
input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except IndexError as exc:
    print(f'{type(exc)} выход за границы списка')
except ValueError as exc:
    print(f'{type(exc)}невозможно преобразовать к числу')
except Exception as exc:
    print(f'{type(exc)} поймано исключение')

#Модифицируйте этот код, обработав исключения для произвольных входных параметров:
#ValueError — невозможно преобразовать к числу,
# IndexError — выход за границы списка, остальные исключения.
# Для каждого типа исключений выведите на консоль соответствующее сообщение.
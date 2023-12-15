# Задача 1. Иконки

Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура его диска: папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.

Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение. Если путь указывает на файл, то также выведите его размер (сколько он весит в байтах). Обеспечьте контроль ввода: проверка пути на существование. 

 

Подсказка: для вывода размера файла поищите соответствующий метод.

 

Пример 1:

Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py

Это файл

Размер файла: 605 байт

 

Пример 2:

Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py

Указанного пути не существует



# Задача 2. Поиск файла

В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории. Однако, как мы понимаем, файлов с таким названием может быть несколько.

Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла, проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.

 

Пример:

Ищем в: C:/Users/Roman/PycharmProjects/Skillbox

Имя файла: lesson2

 

Найдены следующие пути:

C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py

C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py

C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py

C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py

C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py

C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py

C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py

C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py
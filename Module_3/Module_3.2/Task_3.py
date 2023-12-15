print('Задача 3. Кино')


def is_film_exist(movie, movie_list):
    if movie_list.count(movie) > 0:
        return True
    else:
        return False


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня', 'Проклятый остров', 'Начало', 'Матрица']
user_films = []

while True:
    print('\nВаш текущий топ фильмов: ', user_films)
    new_movie = input('Название фильма: ')
    print('Команды: добавить, вставить, удалить')
    command = input('Введите команду: ')
    if command == 'добавить':
        if is_film_exist(new_movie, user_films):
            print('Такой фильм есть в списке!')
        else:
            if is_film_exist(new_movie, films):
                user_films.append(new_movie)
            else:
                print('Такого фильма нет на сайте')
    if command == 'вставить':
        if is_film_exist(new_movie, user_films):
            print('Такой фильм есть в списке!')
        else:
            if is_film_exist(new_movie, films):
                position = int(input('Номер в позиции для фильма: '))
                user_films.insert(position - 1, new_movie)
            else:
                print('Такого фильма нет на сайте')
    if command == 'удалить':
        if is_film_exist(new_movie, user_films):
            print('Такой фильм есть в списке!')
            user_films.remove(new_movie)
        else:
            print('Такого фильма нет в списке!')

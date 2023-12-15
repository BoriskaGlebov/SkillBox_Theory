print('Задача 1. Улучшенная лингвистика 2')

user_words = input('Введите три слова через пробел: ')

words_list = [[x, 0] for x in user_words.split()]
print(words_list[0][0])

us_text = input('введите текст для проверки:')

for ind, word in enumerate(words_list):
    if us_text.count(word[0]) > 0:
        words_list[ind][1] = us_text.count(word[0])
print(words_list)
print(f'Произведена проверка введенной строки и обнаружено:\n'
      f'1 слово ({words_list[0][0]}) встретил {words_list[0][1]} раз\n'
      f'2 слово ({words_list[1][0]}) встретил {words_list[1][1]} раз\n'
      f'3 слово ({words_list[2][0]}) встретил {words_list[2][1]} раз\n'
      )
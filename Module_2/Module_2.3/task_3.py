print('Задача 3. Улучшенная лингвистика')

user_word_list = []
count_list = [0, 0, 0]

for ind in range(3):
    word = input(f'Введите {ind + 1} слово для поиска:')
    user_word_list.append(word)
print(user_word_list)

word_text = input('Слово из текста: ')
while word_text != 'end':
    for i in range(3):
        if word_text == user_word_list[i]:
            count_list[i] += 1
    word_text = input('Слово из текста: ')
print('Подсчёт слов в тексте:')
for i in range(3):
    print(f'{user_word_list[i]}:{count_list[i]}')

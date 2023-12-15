import time
def polindrom(analize_string):
    if analize_string == analize_string[::-1]:
        return True
    else:
        return False


print('Задача 2. Логирование')

line_count = 0
word_file = open('words.txt', 'r', encoding='utf-8')
try:
    for i_line in word_file:
        if i_line.rstrip().isdigit():
            raise ValueError('Там цифра в документе')
        if polindrom(i_line.rstrip('\n')):
            line_count += 1
    print(line_count)
except ValueError as exc:
    print(f'{exc}')
    error = open('errors.txt', 'a', encoding='utf8')
    error.write(str(type(exc)) + str(exc)+time.ctime(time.time())+'\n')
finally:
    word_file.close()
    if error:
        error.close()
print(error.closed)

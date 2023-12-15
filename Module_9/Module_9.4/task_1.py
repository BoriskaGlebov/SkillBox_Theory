print('Задача 1. Сумма чисел')
numbers_file = open('numbers.txt', 'r')
ans_file = open('answer.txt', 'w')
print('Содержимое файла numbers.txt:')
summ = 0
summ_list = []
for el in numbers_file:
    print(el, end='')
    cl_el = el.strip()
    summ += int(cl_el)
ans_file.write(str(summ))
ans_file = open('answer.txt', 'r')
print(ans_file.read())
numbers_file.close()
ans_file.close()
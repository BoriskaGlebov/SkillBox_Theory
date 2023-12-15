from random import randint

print('Задача 2. Студенты')


class Student:
    def __init__(self, surname, name, group_number, estimations):
        self.surname = surname
        self.name = name
        self.group_number = group_number
        self.estimations = estimations

    def average(self):
        estimations_list = [int(el) for el in self.estimations.split()]
        average_score = str(sum(estimations_list) / len(estimations_list))
        return average_score

    def stud_info(self):
        # print(self.surname,
        #       self.name,
        #       self.group_number,
        #       self.estimations,
        #       self.average())
        rez = [self.surname, self.name, self.group_number, self.estimations, '   ' + self.average()]
        return rez


# with open('student.txt', 'w', encoding='utf8') as student_file:
#     for student in range(2):
#         surname = input('Введите фамилию: ')
#         name = input('Введите имя: ')
#         group = input('Введите группу')
#         estimate = ' '.join([str(randint(2, 5)) for _ in range(5)])
#         out_str = '{:<10}*{:<10}*{:<10}*{:<10}'.format(surname, name, group, estimate)
#         student_file.write(out_str + '\n')
with open('student.txt', 'r', encoding='utf8') as student_file:
    student_list = []
    for i__line in student_file:
        stud_file_list = student_file.readline().rstrip().split('*')
        student_list.append(
            Student(stud_file_list[0], stud_file_list[1], stud_file_list[2], stud_file_list[3]).stud_info())
    student_list.sort(key=lambda x: (float(x[4])))
    print('{:<11}{:<11}{:<11}{:<13}'.format('Фамилия','Имя','Группа','Оценки','Ср.балл'))
    for i in student_list:
        print(' '.join(i))

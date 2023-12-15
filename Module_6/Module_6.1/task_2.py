print('Задача 2. Студент')

info_student = input('Введите информацию о студенте через пробел\n'
                     ' (имя, фамилия, город, место учёбы, оценки): '
                     )
info_student_list = info_student.split()
student_dict = {}
student_dict['Имя'] = info_student_list[0]
student_dict['Фамилия'] = info_student_list[1]
student_dict['Город'] = info_student_list[2]
student_dict['Место учебы'] = info_student_list[3]
student_dict['Оценки'] = [int(estimation) for estimation in info_student_list[4:]]
print(student_dict)

for info in student_dict:
    print(info, ' - ', student_dict[info])
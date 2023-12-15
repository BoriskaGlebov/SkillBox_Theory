print('Задача 2. Непонятно!')
type_dict = {
    "<class 'str'>": ('str (строка)', 'Неизменяемый (immutable)'),
    "<class 'dict'>": ('dict (словарь)', 'Изменяемый (mutable)')

}
print(type_dict["<class 'str'>"])

string = 'Привет'
print(string)
print('Тип данных: ', type_dict[str(type(string))][0])
print(type_dict[str(type(string))][1])
print('Id объекта:', id(string))
print()

us_dict = {'a': 10, 'b': 20}
print(us_dict)
print('Тип данных: ', type_dict[str(type(us_dict))][0])
print(type_dict[str(type(us_dict))][1])
print('Id объекта:', id(us_dict))
print()
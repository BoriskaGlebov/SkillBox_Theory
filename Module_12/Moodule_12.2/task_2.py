class Human:
    __count = 0

    def __init__(self, name: str, age: int):
        self.__name = ''
        self.set_name(name)
        self.__age = 0
        self.set_age(age)
        Human.__count += 1

    def set_name(self, name: str):
        if name.isalpha():
            self.__name = name
        else:
            raise 'Должны быть только буквы'

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            raise 'Число должно быть от 0 до 100'

    def get_count(self):
        return Human.__count

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return f'{self.get_name()} {self.get_age()} лет'


print('Задача 2. Человек')

h_1 = Human('Bob', 12)
h_2 = Human('Jo', 36)
print(h_1)
print(h_2)
print(h_1.get_count())


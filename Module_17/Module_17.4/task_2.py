from typing import Any


class Person:
    def __init__(self, name: str, age: int, other: Any) -> None:
        self._name = name
        self._age = age
        self._other = other

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, other):
        self._other = other


print('Задача 2. Сортировка')

user1 = Person('Jon', 45, 'smoking')
user2 = Person('Boris', 18, 'not smoking')
user3 = Person('Arnold', 90, 'drugs')
user_list = [user1, user2, user3]

print(sorted(user_list, key=lambda el: el.age))
for el in sorted(user_list, key=lambda el: el.age):
    print(el)

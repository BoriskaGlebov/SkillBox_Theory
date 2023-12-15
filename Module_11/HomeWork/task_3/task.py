print('Задача 3. Отцы, матери и дети')


class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def feed(self):
        childrens_list = [Children()]

class Children:
    calm = False
    satisfied = True
    def __init__(self,name,age,calm,satisfied):
        self.name = name
        self.age = age
        self.calm = calm
        self.satisfied = satisfied





class Robot:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)


class VacuumCleaner(Robot):
    def __init__(self, model, trash_bag=0):
        super().__init__(model)
        self.trash_bag = trash_bag

    def operate(self):
        print('Я пылесошу пол')
        self.trash_bag += 1
        print(f'Наполненность мусорного мешка = {self.trash_bag}')


class MilRobot(Robot):
    def __init__(self, model, guns):
        super().__init__(model)
        self.guns = guns

    def operate(self):
        print(f'Защищаю военную базу c помощью {self.guns}')


class Submarine(MilRobot):
    def __init__(self, model: str, guns: str, deep: int):
        super().__init__(model, guns)
        self.deep = deep

    def operate(self):
        super().operate()
        print('Охрана ведется под водой')


print('Задача 2. Роботы')

rob = Robot('T-100')
print(rob)
rob_1 = VacuumCleaner('D_500')
print(rob_1)
rob_1.operate()
rob_2 = MilRobot('gd-erwt', 'Пушки')
print(rob_2)
rob_2.operate()
rob_3 = Submarine('sasd ada', 'Торпеды', 10)
print(rob_3)
rob_3.operate()

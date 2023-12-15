class Ship:
    def __init__(self, model):
        self.model = model

    def sail(self):
        print('Корабль плывет........')

    def __str__(self):
        return f'Корабль c моделью {self.model}'


class WarShip(Ship):
    def __init__(self, guns, model):
        super().__init__(model)
        self.guns = guns

    def atack(self):
        print(f'{self.__str__()} атакуют с помощью {self.guns}')


class CargoShip(Ship):
    def __init__(self, model, fullness=0):
        super().__init__(model)
        self.fullness = fullness

    def load(self):
        print('Идет погрузка')
        self.fullness += 1

    def unload(self):
        print('Идет разгрузка')
        self.fullness -= 1


print('Задача 1. Корабли')

ship_1 = Ship('lt100')
print(ship_1)
ship_1.sail()

ship_2 = WarShip('пушки', 'T-1000')
print(ship_2)
ship_2.atack()
ship_2.sail()

ship_3 = CargoShip('ML-102345')
print(ship_3)
print(ship_3.fullness)
ship_3.sail()
ship_3.load()
print(ship_3.fullness)
ship_3.load()
print(ship_3.fullness)
ship_3.unload()
print(ship_3.fullness)
ship_3.sail()

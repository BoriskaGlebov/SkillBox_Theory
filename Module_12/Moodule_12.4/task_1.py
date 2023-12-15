class Unit:
    def __init__(self, hitpoint):
        self.__hitpoint = hitpoint

    def get_hitpoint(self):
        return self.__hitpoint

    def set_hitpoint(self, hitpoint):
        self.__hitpoint = hitpoint

    def atack(self, damage=0):
        self.__hitpoint -= 0

    def __str__(self):
        return f'{self.__class__.__name__}\tздоровье = {self.__hitpoint}'


class Solder(Unit):
    def atack(self, damage=0):
        self.set_hitpoint(self.get_hitpoint() - damage)
        return self.get_hitpoint()


class Civillian(Unit):
    def atack(self, damage=0):
        self.set_hitpoint(self.get_hitpoint() - 2 * damage)
        return self.get_hitpoint()


print('Задача 1. Юниты')

un = Unit(100)
print(un)
un.atack(52)
print(un)
sold = Solder(100)
print(sold)
sold.atack(50)
print(sold)
civ = Civillian(100)
print(civ)
civ.atack(45)
print(civ)

class CanFly:
    def __init__(self):
        self.altitude = 0
        self.speed = 0

    def fly_up(self):
        pass

    def fly(self):
        pass

    def ground(self):
        self.altitude = 0
        self.speed = 0
        return f'Приземлился скорость = {self.speed}\tВысота = {self.altitude} '

    def __str__(self):
        return (f'{self.__class__.__name__}\n'
                f'Высота = {self.altitude} метров\tСкорость = {self.speed} км/ч')


class ButterFly(CanFly):
    def fly_up(self, altitude):
        self.altitude = altitude
        return f'Бабочка взлетела высота {self.altitude} метров'

    def fly(self, speed):
        self.speed = speed
        return f'Бабочка летит со скоростью = {self.speed} км/ч'


class Racket(CanFly):
    def fly_up(self, altitude, speed):
        self.altitude = altitude
        self.speed = speed
        return f'{self.__class__.__name__} Взлетела высоа = {self.altitude} скорость = {self.speed}'

    def ground(self):
        return f'{super().ground()} БА-бах!!!'

    def babah(self):
        return f'Ракета БА-бах!!!!'



print('Задача 2. Полёт')

# but_1 = ButterFly()
# print(but_1)
# print(but_1.fly_up(100))
# print(but_1)
# print(but_1.fly(0.5))
rack = Racket()
print(rack)
print(rack.fly_up(500, 1000))
print(rack.ground())
print(rack.babah())

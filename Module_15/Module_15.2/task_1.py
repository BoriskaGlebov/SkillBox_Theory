class Robot:
    def __init__(self, model: str = '0000', *args):
        super().__init__()
        self.model = model

    def greeting(self) -> str:
        return f'Я — Робот'


class Can_Fly:
    def __init__(self, *args) -> None:
        self.can_fly: bool = True
        self.altitude: float = 0
        self.speed: float = 0

    def fly_up(self, speed: float) -> None:
        self.speed = speed
        print(f'Взлетаю со скоростью {self.speed} км/ч')

    def fly(self, altitude: float, speed: float) -> None:
        self.altitude = altitude
        self.speed = speed
        print(f'Я лечу на высоте {self.altitude} км '
              f'со скоростью {self.speed} км/ч')

    def ground(self, altitude: float = 0, speed: float = 0) -> None:
        self.speed = speed
        self.altitude = altitude
        print(f'Я приземлился высота = {self.altitude}'
              f'скорость = {self.speed}')


class Scout_Drone(Robot, Can_Fly):

    def operate(self) -> None:
        print('Веду разведку с воздуха')
        print('Передвинулся немного вперед')


class Mill_Drone(Robot, Can_Fly):
    def __init__(self, model: str, guns: str) -> None:
        super().__init__(model)
        self.guns = guns

    def operate(self) -> None:
        print(f'Защищаю военный объект с помощью {self.guns}')


print('Задача 1. Снова роботы')

t1000 = Mill_Drone('T-1000', 'Вандервафля')
print(t1000.model)
t1000.fly_up(500)
t1000.fly(500, 1000)
t1000.ground()
t1000.operate()
print(t1000.greeting())
print()

lukas = Scout_Drone('Lukas_Drone')
print(lukas.model)
lukas.fly_up(500)
lukas.fly(500, 1000)
lukas.ground()
lukas.operate()
print(lukas.greeting())


from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color: str, speed: int) -> None:
        self.color = color
        self.speed = speed

    @abstractmethod
    def moving(self, speed) -> None:
        self.speed = speed
        print(f'Транспорт поехал со скоростью {self.speed}')

    # @abstractmethod
    def signal(self) -> None:
        print('Бип- бип')


class MusicMixin:
    def musik_on(self):
        print('Бам - ба - лей - ла')


class Auto(Transport):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)
        self.move = 'Ездит только по земле'

    def moving(self, speed:int) -> None:
        super().moving(speed)


class Ship(Transport):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)
        self.move = 'Ездит только по воде'

    def moving(self, speed: int) -> None:
        super().moving(speed)


class Amfibia(Transport, MusicMixin):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)
        self.move = 'Ездит и по воде и по земле'

    def moving(self, speed: int) -> None:
        super().moving(speed)


print('Задача 1. Транспорт')

boris_auto = Auto('red', 200)
print(boris_auto.move)
boris_auto.moving(100)
boris_auto.signal()
print()
boris_ship = Ship('white', 10)
print(boris_ship.move)
boris_ship.moving(500)
boris_ship.signal()
print()
boris_amfibia = Amfibia('green', 1510)
print(boris_amfibia.move)
boris_amfibia.moving(1000)
boris_amfibia.signal()
boris_amfibia.musik_on()
# boris_transport = Transport('Orange', 789)

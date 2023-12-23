from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color: str, speed: int) -> None:
        self._color = color
        self.speed = speed

    @abstractmethod
    def moving(self, speed) -> None:
        self.speed = speed
        print(f'Транспорт поехал со скоростью {self.speed}')

    # @abstractmethod
    def signal(self) -> None:
        print('Бип- бип')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class MusicMixin:
    def musik_on(self):
        print('Бам - ба - лей - ла')


class Auto(Transport):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)
        self.move = 'Ездит только по земле'

    def moving(self, speed: int) -> None:
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


c = Amfibia('red', 100)
print(c.color)
c.color = 'yellow'
print(c.color)

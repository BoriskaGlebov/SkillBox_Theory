from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x: int, y: int, length: int, width: int):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def moving(self, x, y):
        self.x += x
        self.y += y

    @abstractmethod
    def resizing(self, length, width):
        self.length += length
        self.width += width


class Square(Figure):
    def __init__(self, x, y, length):
        super().__init__(x, y, length, length)

    def resizing(self, length):
        super().resizing(length, length)


class Rectangle(Figure):
    def __init__(self, x, y, length, width):
        super().__init__(x, y, length, width)

    def resizing(self, length, width):
        super().resizing(length, width)


print('Задача 2. Фигуры')

d = Square(1, 2, 10)
print(d.x, d.y)
print(d.length, 'x', d.width)
d.moving(15, 26)
print(d.x, d.y)
d.resizing(50)
print(d.length, 'x', d.width)
print()

g = Rectangle(1, 2, 10, 36)
print(g.x, g.y)
print(g.length, 'x', g.width)
g.moving(15, 26)
print(g.x, g.y)
g.resizing(2, 3)
print(g.length, 'x', g.width)

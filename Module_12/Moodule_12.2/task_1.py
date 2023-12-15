class Point:
    def __init__(self, x: int, y: int):
        self.__x = 0
        self.__y = 0
        self.set_x(x)
        self.set_y(y)

    def __str__(self):
        return f'Точка с координатами x= {self.__x}, y = {self.__y}'

    def set_x(self, x: int):
        if isinstance(x, int):
            self.__x = x
        else:
            raise "Введи число а не строку"

    def set_y(self, y: int):
        if isinstance(y, int):
            self.__y = y
        else:
            raise "Введи число а не строку"

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


print('Задача 1. Координаты точки')
d = Point(1, 2)
print(d)
d.set_x(123)
print(d)

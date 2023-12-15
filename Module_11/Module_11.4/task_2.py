print('Задача 2. Координаты точки')


class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1

    def info(self):
        print(f'x= {self.x}\n'
              f'y= {self.y}')


moskow = Point(15, 45)
kolona = Point(66, 156)
piter = Point(123, 1245)

print(Point.count)

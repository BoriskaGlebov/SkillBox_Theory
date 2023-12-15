print('Задача 1. Машина 3')


class Toyota:
    def __init__(self, car_color='red', car_price=1e6, max_speed=200, current_speed=0):
        self.car_color = car_color
        self.car_price = car_price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info(self):
        print(f'Цвет машины: {self.car_color}\n'
              f'Цена машины: {self.car_price}\n'
              f'Максимальная скорость: {self.max_speed}\n'
              f'Текущая скорость: {self.current_speed}')


car = Toyota('green', ' ',150, 0)
car.info()

import  random
print('Задача 1. Машина 2')


class Toyota:
    car_color = 'красный'
    car_price = 1000000
    max_speed = 200
    current_speed = 0

    def info(self):
        print(f'Цвет машины: {self.car_color}\n'
              f'Стоимость машины: {self.car_price}\n'
              f'Максимальная скорость:{self.max_speed}\n'
              f'Текущая скорость: {self.current_speed}')

    def current_speed_changer(self, speed):
        self.current_speed = speed



car_1 = Toyota()
car_1.info()
car_1.current_speed_changer(random.randint(0,200))
car_1.info()
print(Toyota.current_speed)



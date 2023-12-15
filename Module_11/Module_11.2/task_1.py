import random

print('Задача 1. Машина')


class Toyota:
    car_color = 'красный'
    car_price = 1000000
    max_speed = 200
    current_speed = 0


car_1 = Toyota
car_1.current_speed = random.randint(0, 200)
car_2 = Toyota()
car_2.current_speed = random.randint(0, 200)
car_3 = Toyota()
car_3.current_speed = random.randint(0, 200)
car_4 = Toyota()
car_4.current_speed = random.randint(0, 200)
print(car_1.current_speed, car_2.current_speed, car_3.current_speed, car_4.current_speed)

print(type(car_1))

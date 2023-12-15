print('Задача 1. Зоопарк')

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
print('Зоопарк:', zoo)
new_animal = 'bear'
new_ind = zoo.index('lion')
zoo.insert(new_ind + 1, new_animal)
print(zoo)
zoo.remove('elephant')
print(zoo)
print('Лев сидит в клетке номер', zoo.index('lion') + 1)
print('Обезьяна сидит в клетке номер', zoo.index('monkey') + 1)

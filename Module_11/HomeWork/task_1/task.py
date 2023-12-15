from random import randint
from time import sleep

print('Задача 1. Драка')


class Warrior:
    def __init__(self, health=100, damage=20):
        self.health = health
        self.damage = damage

    def attack(self, damage):
        self.health -= damage

    def print_info(self):
        if self.health >= 0:
            print(f'Осталось здоровья: {self.health}')
        else:
            print(f'Осталось здоровья: 0')


warrior_1 = Warrior()
warrior_2 = Warrior()
while warrior_1.health > 0 and warrior_2.health > 0:
    who = randint(1, 2)
    print('Дыщ!!!!')
    if who == 1:
        print('Воин_1 ударил Воина_2')
        warrior_2.attack(warrior_1.damage)
        warrior_2.print_info()
        print()
    elif who == 2:
        print('Воин_2 ударил Воина_1')
        warrior_1.attack(warrior_2.damage)
        warrior_1.print_info()
        print()
    sleep(2)
if warrior_1.health > warrior_2.health:
    print('Победил warior_1')
else:
    print('Победил warior_2')

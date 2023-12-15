from garden import *

print('Задача 3. Весёлая ферма')

garden_1 = Garden(5)

for _ in range(3):
    garden_1.grow_all()
    garden_1.all_status()
    garden_1.is_ripe()

garden_1.potatoes[0].info_print()

pot = Potato(1)
pot.grow()
pot.info_print()

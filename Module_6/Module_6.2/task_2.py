print('Задача 2. Кризис фруктов')

ncomes = {
            'apple': 5600.20,
            'orange': 3500.45,
            'banana': 5000.00,
            'bergamot': 3700.56,
            'durian': 5987.23,
            'grapefruit': 300.40,
            'peach': 10000.50,
            'pear': 1020.00,
            'persimmon': 310.00,
            }
tot_summ = sum(ncomes.values())
min_value = min(ncomes.values())
min_key = ''
for keys, value in ncomes.items():
    if value == min_value:
        min_key = keys
        break

print('Общий доход за год составил {} рублей'.format(tot_summ))
print('Самый маленький доход у {0} . Он составляет {1} рублей'.format(
    min_key, min_value)
)
ncomes.pop(min_key)
print(ncomes)
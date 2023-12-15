print('Задача 2. Магазин')
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_prices = [(el if el > 0 else 0) for el in original_prices]

print(original_prices)
print(new_prices, sep='')

print('Задача 1. Анализ цен')
import random

# original_prices = [-12, 3, 5, -2, 1]
original_prices = [random.randint(-100, 100) for _ in range(10)]
new_prices = original_prices[:]
new_prices = [(el if el > 0 else 0) for el in new_prices]
print(original_prices)
print(new_prices)
print("Мы потеряли: ", sum(original_prices) - sum(new_prices))

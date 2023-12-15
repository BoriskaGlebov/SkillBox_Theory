print('Задача 3. Повышение цен')
num_roduct = int(input('Сколько товаров: '))
price = [float(input('Цена товара: ')) for _ in range(num_roduct)]
first_up = int(input('Повышение первый год? '))
price_2 = [round(el * ((first_up / 100) + 1), 2) for el in price]
print(price_2)
second_up = int(input('Повышение второй год? '))
price_3 = [round(el * ((second_up / 100) + 1),2) for el in price_2]
print(price_3)
print('Сумма цен за каждый год: ', sum(price), sum(price_2), sum(price_3) )

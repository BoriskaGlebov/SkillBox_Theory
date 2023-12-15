print('Задача 3. Лавка')
goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('Новый фрукт: ')
price = int(input('Цена: '))

print('Текущий ассортимент:', goods)
goods.append([fruit_name, price])
print('Новый ассортимент:', goods)
for good in goods:
    good[1] = round((good[1] * 1.08),2)
print('Новый ассортимент с увел. ценой: ', goods)

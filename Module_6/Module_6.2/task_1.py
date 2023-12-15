print('Задача 1. Склады')

small_storage = {
                'гвозди': 5000,
                'шурупы': 3040,
                'саморезы': 2000
                }
print(small_storage)

big_storage = {
                'доски': 1000,
                'балки': 150,
                'рейки': 600
                }
print(big_storage)

big_storage.update(small_storage)
print(big_storage)

user = input("Что хотите найти?")
print(big_storage.get(user,'Такого товара нет'))

print(sorted(big_storage.keys()))
print(sorted(big_storage.values(),reverse=True))
print(max(big_storage.values()))
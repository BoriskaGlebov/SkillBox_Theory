print('Задача 1. Кубы и квадраты')
left = int(input('Левая граница: '))
right = int(input(('Правая границы: ')))
square = [x ** 2 for x in range(left, right + 1)]
cube = [x ** 3 for x in range(left, right + 1)]

print(f'Список кубов чисел в диапазоне от {left} до {right}: {cube}')
print(f'Список квадратов чисел в диапазоне от {left} до {right}: {square}')

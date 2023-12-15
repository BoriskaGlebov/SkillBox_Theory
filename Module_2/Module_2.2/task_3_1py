print('Задача 3. Собачьи бега')

num_of_dogs = int(input('введите количество собак: '))
dog_points = []

for i in range(num_of_dogs):
    point = int(input(f'Введите очки {i + 1} собаке: '))
    dog_points.append(point)
print(dog_points)
maximum = dog_points[0]
minimum = dog_points[0]
max_ind = -1
min_ind = -1

for i in range(num_of_dogs):
    check = dog_points[i]
    if check > maximum:
        maximum = check
        max_ind = i
    elif check < minimum:
        minimum = check
        min_ind = i
print(maximum, minimum)
print(max_ind, min_ind)
dog_points[max_ind] = minimum
dog_points[min_ind] = maximum
print(dog_points)

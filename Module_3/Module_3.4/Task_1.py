print('Задача 1. Матрица')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for ind in matrix:
    for ind_ind in ind:
        print(ind_ind, end=' ')
    print()

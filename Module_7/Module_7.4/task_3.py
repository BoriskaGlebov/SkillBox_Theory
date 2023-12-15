print('Задача 3. В одну строчку')
print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if i_key % 2 == 0])
print(
    [el
     for key, el in
     {i: el for i, el in zip([i for i in range(5)], [0, 100, 144, 20, 19])}.items()
     if key % 2 == 0
     ]
)

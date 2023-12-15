print('Задача 2. Олимпиада')

num_of_players = int(input('Кол-во участников: '))
num_in_team = int(input('Кол-во человек в команде: '))
team = []
member = 1
if num_of_players % num_in_team:
    print(f'{num_of_players} не возможно поделить на команды по {num_in_team} человек')
else:
    for _ in range(num_of_players // num_in_team):
        team.append(list(range(member, member + 4)))
        member +=num_in_team


# team = list(range(1, num_of_players + 1))
print(team)

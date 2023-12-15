print('Задача 2. Игроки')

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

# dream_team = [
#     player['name']
#     for player in players_dict.values()
#     if player['team'] == 'A' and player['status'] == 'Rest'
#             ]
#
# print(dream_team)
team_order = ['A', 'B', 'C']
help_dict = {
    'Rest': 'Отдыхает',
    'Training': 'Тренируется',
    'Travel': 'Путешествует'
}
index = 0
for state in help_dict:
    print(f'Все члены команды {team_order[index]}, которые {help_dict[state]}:')
    print([values['name']
           for values in players_dict.values()
           if values['team'] == team_order[index] and
           values['status'] == state])
    index += 1
    # for values in players_dict.values():
    #     if values['status'] == state and values['team'] == team_order[index]:
    #         print(values['name'])
    # index += 1

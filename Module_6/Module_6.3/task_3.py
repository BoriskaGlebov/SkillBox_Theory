# {
#     'server': {
#         'host' : '127.0.01',
#         'port': '10'
#               },
#     'configuration': {
#         'ssh': {
#             'access': 'true',
#             'login': 'Ivan',
#             'password': 'qwerty'
#         }
#     }
# }

data = dict()
data['server'] = {
    'host': '127.0.01',
    'port': '10'
}
data['configuration'] = {
    'ssh': {
        'access': 'true',
        'login': 'Ivan',
        'password': 'qwerty'
    }
}

# print(data)
# print(data['server']['port'])
# data['configuration']['ssh']['login'] = 'Boris'
# print(data['configuration']['ssh']['login'])
print()
for i_value in data.values():
    # print(i_value)
    for j_key in i_value:
        print(j_key, i_value[j_key])
print('Задача 2. Сервер')

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
print(type(server_data['server']['host']))
for key, value in server_data.items():
    print(f'{key}:\n')
    for k,v in value.items():
        print(f'\t{k}: {v}')
    print()

import requests
import json

print('Задача 1. Звёздные войны')
my_requests = requests.get('https://swapi.dev/api/people/3/')
data = json.loads(my_requests.text)
data['name'] = 'ЧУШПАН-R22-D22'
print(data['name'])
with open('test1.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
my_requests_2 = requests.get('https://swapi.dev/api/planets/8/')
data2 = json.loads(my_requests_2.text)
with open('test2.json', 'a', encoding='utf-8') as file:
    json.dump(data2, file, indent=4, ensure_ascii=False)

# print(my_requests)
# print(type(my_requests.text))
#
# data = json.loads(my_requests.text)
# print(type(data))
#
# with open('file.json', 'w') as file:
#     json.dump(data, file, indent=4)
#
# with open('file.json', 'r') as file:
#     data = json.load(file)
# print(data)

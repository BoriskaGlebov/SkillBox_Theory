import requests
import json

print('Задача 2. Документация API')
my_request = requests.get('https://swapi.dev/api/films/1/')
json_dict = json.loads(my_request.text)
print(json_dict['opening_crawl'])

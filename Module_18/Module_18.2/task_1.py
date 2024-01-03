import re

print('Задача 1. Скороговорка')

user_text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
print(user_text)
print('1. Найти первое упоминание шаблона wo в тексте.')
print(re.match(r'wo', user_text))
print('2. Определить содержимое найденной по шаблону подстроки из пункта 2.')
print(re.search(r'wo', user_text))
print('3. Найти позицию, с которого начинается первое упоминание шаблона wo.')
print(re.search(r'wo', user_text).start())
print('4. Найти позицию, на которой заканчивается первое упоминание шаблона wo.')
print(re.search(r'wo', user_text).end())
print('5. Получить список из каждого упоминания шаблона wo в тексте.')
print(re.findall(r'wo',user_text))
print('6. Заменить в тексте все совпадения по шаблону wo на слово «ЗАМЕНА».')
print(re.sub(r'wo',"ЗАМЕНА", user_text))
print('7. По каждому действию вывести соответствующий результат. '
      'Не используйте методы строк. '
      'Не забывайте использовать приписку r в шаблонах.')

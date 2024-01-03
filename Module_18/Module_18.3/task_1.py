import re

print('Задача 1. Согласные')
user_text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
print(re.findall(r'\b[aoeiuyAOEIUY]\w*', user_text))
print(re.findall(r'\b[^aoeiuyAOEIUY\W]\w+', user_text))
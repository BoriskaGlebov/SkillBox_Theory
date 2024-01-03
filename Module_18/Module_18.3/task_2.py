import re

print('Задача 2. Даты')

user_str = ('Amit 34-3456 12-05-2007, '
            'XYZ 56-4532           11-11-2011, '
            'ABC 67-8945 12-01-2009')

print(re.findall(r'\d{2}-\d{2}-\d{4}', user_str))
print(re.findall(r'\b[^\d\W]\w+?', user_str))
print(re.findall(r'\b\d+\W+\d+[\S]\w\d+', user_str))
print(re.sub(r'\s+','*',user_str))
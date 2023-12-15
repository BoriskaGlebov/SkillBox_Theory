print('Задача 1. Пунктуация')

text = 'Я! Есть. Грут?! Я, Грут и Есть.'
text = set(text)
set_2 = '.,;:!?'
set_2 = set(set_2)
print(text, type(text), len(text))
print(set_2, type(set_2), len(set_2))
print('Количество знаков пунктуации:', len(text.intersection(set_2)))
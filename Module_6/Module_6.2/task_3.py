def histogramma(string):
    histogramma = {}
    for letter in string:
        if histogramma.get(letter):
            histogramma[letter] += 1
        else:
            histogramma[letter] = 1
    return histogramma


print('Задача 3. Гистограмма частоты')

user_text = input('Введите текст: ')
hist = histogramma(user_text)
print(hist)

for key in sorted(hist):
    print(key, ':', hist[key])
print('Максимальная частота:', max(hist.values()))
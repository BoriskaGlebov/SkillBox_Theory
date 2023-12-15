print('Задача 1. Бесконечный генератор')


def counter():
    n = 0
    while True:
        yield n
        n += 1


def prime_num(n=50):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


d = prime_num()
for num in d:
    print(num)
import math
def factorial_my(num):
    if num == 1:
        return 1
    rez = num * factorial_my(num - 1)
    return rez


print('Задача 1. Challenge')

number = 10



print(factorial_my(number))
print(math.factorial(number))

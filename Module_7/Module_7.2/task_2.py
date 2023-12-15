import math
def form(r,h):
    side = 2 * math.pi * r * h
    s = 2 * math.pi * r
    s_ful = side + 2 * (2 * math.pi * r)
    return side, s, s_ful


print('Задача 2. Цилиндр')


r = float(input('Введи радиус: '))
h = float(input('Введи высоту: '))
rez = form(r,h)
print('Площадь боковой поверхности ({r:.2f} — радиус, {h:.2f} — высота): {rez:.2f}'.format(
    r=r,
    h=h,
    rez=rez[0]
))
print('Полная площадь ({S:.2f} — площадь круга): {rez:.2f}'.format(
    S=rez[1],
    rez=rez[2]
))
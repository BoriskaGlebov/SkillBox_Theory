a = [1, 2, 3, 4, 5, 6]
print(a)

for n, i in enumerate(a):
    a[n] += 10
print(a)
b = lambda x: x + 10
print(b(5))
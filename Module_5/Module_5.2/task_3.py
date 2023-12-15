print('Задача 3. IP-адрес')
oct = []
for num in range(4):
    octet = int(input('введи число:'))
    while octet > 255:
        print('ошибка число должно быть до 255')
        octet = int(input('введи число:'))
    oct.append(octet)

print(oct)
# ip_address = 'Пример правильного адреса: {0}.{1}.{2}.{3}'.format(
#     oct[0],oct[1],oct[2],oct[3]
# )
ip_address = 'Пример правильного адреса: {0}.{1}.{2}.{3}'.format(
    *oct
)
print(ip_address)
print('Задача 3. Пакеты')
num_of_packs = int(input('Кол-во пакетов: '))
code = []
decode = []
lost_pack = 0

for number in range(num_of_packs):
    print(f'\nПакет номер {number + 1} ')
    for num_bit in range(4):
        bits = int(input(f'{num_bit + 1} бит:'))
        code.append(bits)
    if code.count(-1) > 1:
        lost_pack += 1
        print('Слишком много ошибок в пакете!')
    else:
        decode.extend(code)
    code = []
print('Полученное сообщение:', decode)
print('Кол-во ошибок в сообщении:', decode.count(-1))
print('Кол-во потерянных пакетов:', lost_pack)

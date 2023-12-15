print('Задача 2. Однотипные объекты')


class Monitor:
    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 60


class HeadPhones:
    headphones_name = 'Sony'
    headphones_sensitivity = 108
    headphones_micro = True


monitors = [Monitor() for _ in range(4)]
for ind, freq in enumerate([60, 144, 70, 60]):
    monitors[ind].monitor_freq = freq
headPhones = [HeadPhones() for _ in range(3)]
headPhones[0].headphones_micro = False



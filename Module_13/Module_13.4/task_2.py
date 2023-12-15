import random


class AlexIter:
    def __init__(self, limit):
        self.count_limit = limit
        self.current_num = 0
        self.next_num = 0

    def __next__(self):
        if self.count_limit:
            if self.next_num == 0:
                self.current_num = random.random()
                self.next_num += self.current_num
                self.count_limit -=1
                return round(self.current_num,2)
            else:
                self.current_num = random.random()
                self.next_num += self.current_num
                self.count_limit -= 1
                return round(self.next_num,2)
        else:
            raise StopIteration

    def __iter__(self):
        return self


print('Задача 2. Случайная сумма')
#
# d = AlexIter(100)
# for d in range(5):
#     print(el)
# print()

d = AlexIter(6)
for el in d:
    print(el)
print(10 in d)

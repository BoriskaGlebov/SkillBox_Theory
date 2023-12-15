class Primes:

    def __init__(self, n):
        self.limit = n
        self.prime_num = 2
        self.current_num = 1

    def __iter__(self):
        self.prime_num = 2
        self.current_num = 1
        return self

    def __next__(self):
        while self.current_num <= self.limit:
            self.current_num += 1
            if self.current_num == 2:
                self.prime_num = self.current_num
                return self.prime_num
            for num in range(2, self.current_num):
                if self.current_num % num == 0:
                    break
            else:
                self.prime_num = self.current_num
                return self.prime_num
        else:
            raise StopIteration


print('Задача 3. Простые числа')

prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')
print(5 in prime_nums)

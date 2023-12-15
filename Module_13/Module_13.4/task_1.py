class CountIterator:
    def __init__(self):
        self.__count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__count += 1
        return self.__count

    # def __str__(self):
    #     out_str = ''
    #     for i in self.__iter__():
    #         out_str += str(i) + ' '
    #     return out_str


print('Задача 1. Бесконечный итератор')
my_iter = CountIterator()
print(my_iter)
for i_elem in my_iter:
    print(i_elem)

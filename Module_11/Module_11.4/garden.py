class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.status = 0

    def grow(self):
        if self.status < 3:
            self.status += 1

    def is_ripe(self):
        if self.status == 3:
            return True
        return False

    def info_print(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.status]}')


class Garden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картоха растет')
        for potato in self.potatoes:
            potato.grow()

    def potatoes_status(self):
        for potato in self.potatoes:
            potato.info_print()

    def all_status(self):
        for potato in self.potatoes:
            potato.info_print()

    def is_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False  # такой return поможет получить информацию о зрелости картошки снаружи этого объекта
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

class Family:
    surname = 'Ивановы'
    family_money = 200000
    have_a_hose = False

    def inform(self):
        print(f'Фамилия: {self.surname}\n'
              f'Сколько есть денег: {self.family_money:,}\n'
              f'Есть ли дом: {self.have_a_hose}')

    def add_money(self, money):
        self.family_money += money

    def buy_hose(self, house_price, discount=0):
        if self.family_money >= house_price:
            self.family_money -= house_price - house_price * discount / 100
            self.have_a_hose = True
        else:
            print('Не хватает денег')


family_1 = Family()
family_1.inform()
family_1.add_money(500000)
print(family_1.family_money)
family_1.inform()
print(family_1.family_money)
family_1.buy_hose(600_000, 10)
family_1.inform()

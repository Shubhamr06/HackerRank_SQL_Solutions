class cars():

    def __init__(self, price, model, yearm):
        self.price = price
        self.model = model
        self.yearm = yearm

    def price_inc(self):
        self.price=int(self.price * 1.15)

    def year_inc(self):
        self.yearm=(self.yearm+1)


honda = cars(100000, 'city', 2017)
tata = cars(60000, 'bolt', 2016)

print(honda.price)
honda.price_inc()
print(honda.price)
print(honda.yearm)
honda.year_inc()
print(honda.yearm)


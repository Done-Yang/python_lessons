class ManuItem():
    def __init__(self, manu, price):
        self.manu = manu
        self.price = price

    def __str__(self):
        return ("Manu: {}, Price: {}".format(self.manu, self.price))

berker = ManuItem("hamberker", 50000)
cake = ManuItem("cake", 30000)
fries= ManuItem("french fries", 45000)

print(berker)
print(cake)
print(fries)
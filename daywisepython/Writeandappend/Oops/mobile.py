class Mobile:
    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

m1 = Mobile("Samsung", "S24", 50000)
m2 = Mobile("Apple", "iPhone 15", 60000)
m3 = Mobile("OnePlus", "12", 45000)

print(m1.company, m1.model, m1.price)
print(m2.company, m2.model, m2.price)
print(m3.company, m3.model, m3.price)
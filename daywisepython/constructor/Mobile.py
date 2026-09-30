class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

m = Mobile("Samsung", "S25", 150000)

print(m.brand)
print(m.model)
print(m.price)
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

c1 = Car("Toyota", "Innova", 2000000)

print(c1.brand)
print(c1.model)
print(c1.price)
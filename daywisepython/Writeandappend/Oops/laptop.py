class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

l1 = Laptop("HP", "8GB", "i5", 55000)

print(l1.brand)
print(l1.ram)
print(l1.processor)
print(l1.price)
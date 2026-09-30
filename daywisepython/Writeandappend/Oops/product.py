class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

p1 = Product("Laptop", 50000, 2)

print(p1.name)
print(p1.price)
print(p1.quantity)
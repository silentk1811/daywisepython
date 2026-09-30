class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    @property
    def total_price(self):
        return self.price * self.quantity

p1 = Product(50, 3)
print(p1.total_price)
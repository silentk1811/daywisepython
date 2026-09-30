class ShoppingCart:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_bill(self):
        print("Total Bill:", self.price * self.quantity)

s = ShoppingCart("Shoes", 2000, 2)
s.total_bill()
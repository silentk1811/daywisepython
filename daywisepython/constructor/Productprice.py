class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self):
        discount_amount = self.price * self.discount / 100
        final = self.price - discount_amount

        print("Final Price:", final)

p = Product("Bag", 1000, 20)
p.final_price()
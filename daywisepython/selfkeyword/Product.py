class Product:
    def __init__(self):
        self.price = 500

    def total(self, number):
        print(self.price * number)

p1 = Product()
p1.total(3)
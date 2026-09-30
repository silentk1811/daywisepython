class Product:
    def __init__(self):
        self.price = 1000
        self.quantity = 2

    def display(self):
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        total = self.calculate_total()
        return total - (total * 10 / 100)


pro = Product()

pro.display()
print("Total:", pro.calculate_total())
print("After Discount:", pro.apply_discount())
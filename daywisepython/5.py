class Product:
    
    def __init__(self):
        self.__price = 0

    def set_price(self, price):

        if price > 0:
            self.__price = price
        else:
            print("Price cannot be zero or negative")

    def display(self):
        print("Price:", self.__price)


product = Product()

product.set_price(500)
product.display()
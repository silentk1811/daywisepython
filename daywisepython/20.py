class ShoppingCart:
    
    def __init__(self):
        self.__items = []
        self.__total = 0

    def add_product(self, product, price):
        self.__items.append(product)
        self.__total = self.__total + price

    def remove_product(self, product, price):

        if product in self.__items:
            self.__items.remove(product)
            self.__total = self.__total - price

    def display(self):
        print("Items:", self.__items)
        print("Total:", self.__total)


cart = ShoppingCart()

cart.add_product("Shirt", 500)
cart.add_product("Shoes", 1000)

cart.remove_product("Shirt", 500)

cart.display()
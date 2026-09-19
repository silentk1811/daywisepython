class Mobile:
    
    def __init__(self):
        self.__brand = ""
        self.__model = ""
        self.__price = 0

    def set_details(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def display(self):
        print("Brand:", self.__brand)
        print("Model:", self.__model)
        print("Price:", self.__price)


mobile = Mobile()

mobile.set_details("Samsung", "A15", 15000)
mobile.display()
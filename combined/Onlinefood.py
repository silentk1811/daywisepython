from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount}rs using UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount}rs using Card")

class Order:
    def __init__(self, item, price):
        self.item = item
        self.__price = price

    def get_price(self):
        return self.__price

order = Order("Pizza", 299)
payment = UPI()
payment.pay(order.get_price())
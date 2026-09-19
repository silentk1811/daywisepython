class Payment:
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class CardPayment(Payment):
    def pay(self):
        print("Paid using Card")

UPI().pay()
CardPayment().pay()
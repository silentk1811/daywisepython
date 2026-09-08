class Customer:
    def show_customer(self):
        print("Customer details")

    def place_order(self):
        print("Order placed")

    def cancel_order(self):
        print("Order cancelled")

cus = Customer()
cus.show_customer()
cus.place_order()
cus.cancel_order()
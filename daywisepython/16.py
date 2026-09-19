class BankCustomer:
    
    def __init__(self):
        self.__name = "Kalyani"
        self.__pin = 1234

    def verify_pin(self, pin):

        if pin == self.__pin:
            print("PIN is correct")
        else:
            print("Wrong PIN")


customer = BankCustomer()

customer.verify_pin(1234)
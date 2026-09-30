class ATM:
    
    def __init__(self):
        self.__balance = 5000
        self.__pin = 1234

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Amount deposited")

    def withdraw(self, amount, pin):

        if pin == self.__pin:

            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Amount withdrawn")
            else:
                print("Insufficient balance")

        else:
            print("Wrong PIN")

    def balance_inquiry(self):
        print("Balance:", self.__balance)


atm = ATM()

atm.deposit(1000)
atm.withdraw(2000, 1234)
atm.balance_inquiry()
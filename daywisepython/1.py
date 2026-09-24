class Bankaccount:
    def __init__(self):
        self.__balance=0
    def deposite(self,amount):
        self.__balance=self.__balance+amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
        else:
            print("Insufficient balance")
    def display(self):
        print("Balance:",self.__balance)            
account=Bankaccount()
account.deposite(5000)
account.withdraw(1000)
account.display()

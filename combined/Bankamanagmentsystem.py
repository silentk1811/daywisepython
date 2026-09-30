from abc import ABC, abstractmethod
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Kalyani")
acc.deposit(5000)
acc.withdraw(1200)
print("Balance:", acc.get_balance())

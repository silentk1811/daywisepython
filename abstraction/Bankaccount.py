from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 1000
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Not enough balance")

acc = SavingsAccount()
acc.withdraw(300)
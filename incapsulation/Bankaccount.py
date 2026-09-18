class BankAccount:
    def __init__(self):
        self.__balance = 0        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(1000)
acc.withdraw(300)
print("Balance:", acc.get_balance())
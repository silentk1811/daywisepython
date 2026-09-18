class Bank:
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display_balance(self):
        print("Balance:", self.balance)

bank = Bank()

bank.deposit(500)
bank.withdraw(200)
bank.display_balance()
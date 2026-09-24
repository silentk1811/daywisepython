class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

b = BankAccount("Kalyani", 5000)

b.deposit(1000)
b.withdraw(500)
b.display()
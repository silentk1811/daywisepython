class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

b1 = BankAccount("Kalyani", 5000)
b2 = BankAccount("Kartiki", 7000)
b3 = BankAccount("sejal", 10000)

b1.display()
b2.display()
b3.display()
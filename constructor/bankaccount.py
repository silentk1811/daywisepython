class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def display(self):
        print("Account No:", self.account_no)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)

acc = BankAccount(12345, "Kalyani", 10000)
acc.display()
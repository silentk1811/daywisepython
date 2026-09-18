class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

account = BankAccount("Kalyani", "1234567890", 10000)

print(account.name)
print(account.account_number)
print(account.balance)
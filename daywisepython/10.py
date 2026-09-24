class Account:
    
    def __init__(self):
        self.__account_number = 0
        self.__balance = 0

    def set_details(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def display(self):
        print("Account Number:", self.__account_number)
        print("Balance:", self.__balance)


account = Account()

account.set_details(12345, 5000)
account.display()
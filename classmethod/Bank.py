class Bank:
    bank_name = "SBI"

    @classmethod
    def change_bank(cls, new_name):
        cls.bank_name = new_name

print(Bank.bank_name)
Bank.change_bank("HDFC")
print(Bank.bank_name)
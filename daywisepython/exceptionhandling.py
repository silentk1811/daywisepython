bike = input("Is bike available? yes/no: ")
if bike == "yes":
    print("I went to bank by bike")
else:
    print("Father took the bike")
    print("I took a rickshaw")
    try:
        raise Exception("Rickshaw driver does not accept online payment")
    except Exception as e:
        print(e)
        print("I paid by cash")



number = input("Enter account number: ")
while number != "12345":
    try:
        raise Exception("Wrong account number")
    except Exception as e:
        print(e)
    number = input("Enter account number again: ")
print("Account number is correct")
try:
    raise Exception("Bank is on lunch break")

except Exception as e:
    print(e)
    print("I waited until bank opened")



balance = 2000
amount = int(input("Enter withdrawal amount: "))

while amount > balance:
    try:
        raise Exception("Insufficient balance")

    except Exception as e:
        print(e)

    amount = int(input("Enter smaller amount: "))

print("Withdrawal successful")
print("Amount:", amount)
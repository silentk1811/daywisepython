class Car:
    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

c = Car("Tata", "Punch", 700000)

print(c.company)
print(c.model)
print(c.price)
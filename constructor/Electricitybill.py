class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculate(self):
        if self.units <= 100:
            bill = self.units * 5
        else:
            bill = self.units * 10

        print("Bill:", bill)

e = ElectricityBill("Kalyani", 80)
e.calculate()
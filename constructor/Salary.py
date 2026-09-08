class Salary:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    def calculate(self):
        hra = self.basic * 0.20
        da = self.basic * 0.10
        gross = self.basic + hra + da

        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross)

s = Salary("Kalyani", 30000)
s.calculate()

    
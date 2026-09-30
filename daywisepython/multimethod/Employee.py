class Employee:
    def __init__(self):
        self.salary = 30000

    def display(self):
        print(self.salary)

    def calculate_annual_salary(self):
        return self.salary * 12

    def calculate_bonus(self):
        return self.salary * 10 / 100

emp = Employee()

emp.display()
print("Annual Salary:", emp.calculate_annual_salary())
print("Bonus:", emp.calculate_bonus())
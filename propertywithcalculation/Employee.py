class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    @property
    def annual_salary(self):
        return self.monthly_salary * 12

e1 = Employee(30000)
print(e1.annual_salary)
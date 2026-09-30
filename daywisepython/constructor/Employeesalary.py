class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        print("Annual Salary:", self.salary * 12)

e = Employee("Kalyani", 30000)
e.annual_salary()
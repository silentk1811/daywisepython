class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

e1 = Employee("Rahul", 25000, "IT")

print(e1.name)
print(e1.salary)
print(e1.department)
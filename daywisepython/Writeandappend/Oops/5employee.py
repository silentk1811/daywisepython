class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Amit", 20000)
e2 = Employee("Rahul", 25000)
e3 = Employee("Sneha", 30000)
e4 = Employee("Priya", 28000)
e5 = Employee("Neha", 22000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)
print(e3.name, e3.salary)
print(e4.name, e4.salary)
print(e5.name, e5.salary)
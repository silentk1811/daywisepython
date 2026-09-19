class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

e = Employee("Kalyani", 30000, "IT")

print(e.name)
print(e.salary)
print(e.department)
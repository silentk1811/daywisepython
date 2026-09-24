class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}\nName: {self.name}\nSalary: {self.salary}"

e1 = Employee(101, "Rahul", 35000)
print(e1)
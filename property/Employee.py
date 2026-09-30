class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

e1 = Employee(40000)
print(e1.salary)
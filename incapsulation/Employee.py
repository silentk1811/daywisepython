class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

    def get_salary(self):
        return self.__salary

e1 = Employee()
e1.set_salary(50000)
print("Salary:", e1.get_salary())
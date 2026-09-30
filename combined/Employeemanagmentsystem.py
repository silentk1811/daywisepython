from abc import ABC, abstractmethod
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        return 60000

class Manager(Employee):
    def calculate_salary(self):
        return 90000

emp1 = Developer("Kalyani")
emp2 = Manager("disha")
print(emp1.name, emp1.calculate_salary())
print(emp2.name, emp2.calculate_salary())
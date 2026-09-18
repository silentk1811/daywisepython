from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary: 60000")

Developer().calculate_salary()
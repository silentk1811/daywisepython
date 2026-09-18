class Employee:
    def calculate_salary(self):
        pass

class FullTime(Employee):
    def calculate_salary(self):
        print("Full-time salary: 50000")

class Intern(Employee):
    def calculate_salary(self):
        print("Intern salary: 15000")

FullTime().calculate_salary()
Intern().calculate_salary()
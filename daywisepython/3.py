class Employee:
    
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):

        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")

    def get_salary(self):
        return self.__salary


employee = Employee()

employee.set_salary(25000)

print("Salary:", employee.get_salary())
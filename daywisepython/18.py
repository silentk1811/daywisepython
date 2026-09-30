class Employee:
    
    def __init__(self):
        self.__name = ""
        self.__department = ""
        self.__salary = 0

    def set_details(self, name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary

    def annual_salary(self):
        return self.__salary * 12

    def display(self):
        print("Name:", self.__name)
        print("Department:", self.__department)
        print("Monthly Salary:", self.__salary)
        print("Annual Salary:", self.annual_salary())


employee = Employee()

employee.set_details("Kalyani", "HR", 25000)
employee.display()
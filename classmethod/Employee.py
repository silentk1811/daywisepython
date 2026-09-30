class Employee:
    company_name = "Infosys"

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

print(Employee.company_name)
Employee.change_company("Wipro")
print(Employee.company_name)
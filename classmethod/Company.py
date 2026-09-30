class Company:
    company_name = "Infosys"
    location = "Pune"

    @classmethod
    def change_location(cls, new_location):
        cls.location = new_location

print(Company.location)
Company.change_location("Mumbai")
print(Company.location)
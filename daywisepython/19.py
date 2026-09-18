class HospitalPatient:
    
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__bill = 0

    def set_details(self, name, age):
        self.__name = name
        self.__age = age

    def add_charges(self, amount):
        self.__bill = self.__bill + amount

    def display_bill(self):
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Bill:", self.__bill)


patient = HospitalPatient()

patient.set_details("Kalyani", 20)
patient.add_charges(500)
patient.add_charges(1000)

patient.display_bill()
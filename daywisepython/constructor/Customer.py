class Customer:
    def __init__(self, id, name, mobile, city):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.city = city

    def display(self):
        print(self.id)
        print(self.name)
        print(self.mobile)
        print(self.city)

c = Customer(18, "Kalyani", "9876543210", "Pune")
c.display()
class Student:
    def __init__(self):
        self.m1 = 80
        self.m2 = 70
        self.m3 = 90

    def display(self):
        print("Marks:", self.m1, self.m2, self.m3)

    def calculate_total(self):
        return self.m1 + self.m2 + self.m3

    def calculate_percentage(self):
        return self.calculate_total() / 3


stud = Student()

stud.display()
print("Total:", stud.calculate_total())
print("Percentage:", stud.calculate_percentage())
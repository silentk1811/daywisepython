class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(self.name)
        print(self.age)
        print(self.course)

stud = Student("Kalyani", 20, "BCS")
stud.display()
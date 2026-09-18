class Student:

    def __init__(self):
        self.__name = ""
        self.__marks = 0

    def set_name(self, name):
        self.__name = name

    def set_marks(self, marks):
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks


student = Student()

student.set_name("Kalyani")
student.set_marks(85)

print("Name:", student.get_name())
print("Marks:", student.get_marks())
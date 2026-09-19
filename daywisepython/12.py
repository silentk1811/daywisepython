class StudentResult:
    
    def __init__(self):
        self.__marks1 = 0
        self.__marks2 = 0
        self.__marks3 = 0

    def set_marks(self, marks1, marks2, marks3):
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3

    def total(self):
        return self.__marks1 + self.__marks2 + self.__marks3

    def percentage(self):
        return self.total() / 3

    def grade(self):
        percentage = self.percentage()

        if percentage >= 75:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        else:
            return "Fail"


student = StudentResult()

student.set_marks(80, 70, 90)

print("Total:", student.total())
print("Percentage:", student.percentage())
print("Grade:", student.grade())
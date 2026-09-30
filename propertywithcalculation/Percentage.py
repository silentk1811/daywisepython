class Student:
    def __init__(self, total_marks):
        self.total_marks = total_marks

    @property
    def percentage(self):
        return self.total_marks / 5

s1 = Student(400)
print(s1.percentage)
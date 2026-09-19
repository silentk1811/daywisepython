class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        self._marks = value

s1 = Student(80)
print(s1.marks)
s1.marks = 90
print(s1.marks)
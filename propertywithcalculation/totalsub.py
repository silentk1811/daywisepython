class Student:
    def __init__(self, m1, m2, m3, m4, m5):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    @property
    def total(self):
        return self.m1 + self.m2 + self.m3 + self.m4 + self.m5

s1 = Student(80, 70, 90, 60, 85)
print(s1.total)
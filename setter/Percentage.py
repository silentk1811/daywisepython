class Student:
    def __init__(self, percentage):
        self._percentage = percentage

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        if 0 <= value <= 100:
            self._percentage = value
        else:
            print("Invalid percentage")

s1 = Student(75)
s1.percentage = 85
print(s1.percentage)
s1.percentage = 120
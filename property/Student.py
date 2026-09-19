class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

s1 = Student("Kalyani")
print(s1.name)
class Employee:
    def __init__(self, experience):
        self._experience = experience

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value >= 0:
            self._experience = value
        else:
            print("Experience cannot be negative")

e1 = Employee(3)
e1.experience = 5
print(e1.experience)
e1.experience = -2
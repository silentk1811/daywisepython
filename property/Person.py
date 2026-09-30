class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

p1 = Person(21)
print(p1.age)
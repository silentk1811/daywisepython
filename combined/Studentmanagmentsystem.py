from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self._name = name         

    @abstractmethod
    def show_details(self):
        pass

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks      

    def get_marks(self):
        return self.__marks

    def show_details(self):       
        print(f"Student: {self._name}, Marks: {self.__marks}")

s1 = Student("Kalyani", 90)
s1.show_details()
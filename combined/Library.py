from abc import ABC, abstractmethod
class Book:
    def __init__(self, title):
        self.title = title
        self.__is_issued = False

    def issue(self):
        if not self.__is_issued:
            self.__is_issued = True
            print(f"{self.title} issued")
        else:
            print("Already issued")

    def return_book(self):
        self.__is_issued = False
        print(f"{self.title} returned")

b = Book("Python Basics")
b.issue()
b.return_book()
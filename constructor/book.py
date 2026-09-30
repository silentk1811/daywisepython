class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(self.title, "-", self.author, "-", self.price)

b1 = Book("Python", "Guido", 400)
b2 = Book("Java", "James", 500)
b3 = Book("C++", "Bjarne", 450)

b1.display()
b2.display()
b3.display()
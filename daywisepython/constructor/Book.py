class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b = Book("The art of being alone", "Renuka Gavrani", 200)

print(b.title)
print(b.author)
print(b.price)
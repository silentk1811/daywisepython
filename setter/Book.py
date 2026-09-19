class Book:
    def __init__(self, pages):
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value > 0:
            self._pages = value
        else:
            print("Pages must be greater than 0")

b1 = Book(200)
b1.pages = 300
print(b1.pages)
b1.pages = -10
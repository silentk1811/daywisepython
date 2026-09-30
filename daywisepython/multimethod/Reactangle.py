class Rectangle:
    def __init__(self):
        self.length = 10
        self.width = 5

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


rect = Rectangle()
rect.display()
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        print("Circle area:", 3.14 * self.r * self.r)

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        print("Rectangle area:", self.l * self.b)

Circle(5).area()
Rectangle(4, 6).area()
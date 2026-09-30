class Rectangle:
    def area(self, length, width):
        print("Area:", length * width)

    def perimeter(self, length, width):
        print("Perimeter:", 2 * (length + width))

r = Rectangle()

r.area(10, 5)
r.perimeter(10, 5)
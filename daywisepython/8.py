class Rectangle:
    
    def __init__(self):
        self.__length = 0
        self.__width = 0

    def set_values(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


rectangle = Rectangle()

rectangle.set_values(10, 5)

print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
class Circle:
    
    def __init__(self):
        self.__radius = 0

    def set_radius(self, radius):

        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be greater than 0")

    def display(self):
        print("Radius:", self.__radius)


circle = Circle()

circle.set_radius(5)
circle.display()
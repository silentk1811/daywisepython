class Circle:
    def __init__(self):
        self.radius = 5

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print("Area:", self.area())
        print("Circumference:", self.circumference())


circle = Circle()
circle.display()
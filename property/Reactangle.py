class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

r1 = Rectangle(10, 5)
print(r1.length)
print(r1.width)
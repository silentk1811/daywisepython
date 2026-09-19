class Laptop:
    def __init__(self, ram):
        self._ram = ram

    @property
    def ram(self):
        return self._ram

l1 = Laptop("16GB")
print(l1.ram)
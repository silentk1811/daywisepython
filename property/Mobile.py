class Mobile:
    def __init__(self, brand):
        self._brand = brand

    @property
    def brand(self):
        return self._brand

m1 = Mobile("Samsung")
print(m1.brand)
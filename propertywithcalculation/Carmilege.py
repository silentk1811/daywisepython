class Car:
    def __init__(self, distance, fuel):
        self.distance = distance
        self.fuel = fuel

    @property
    def mileage(self):
        return self.distance / self.fuel

c1 = Car(300, 15)
print(c1.mileage)
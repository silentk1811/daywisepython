class Car:
    
    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        self.__speed = self.__speed + 10

    def brake(self):
        self.__speed = self.__speed - 10

        if self.__speed < 0:
            self.__speed = 0

    def display(self):
        print("Speed:", self.__speed)


car = Car()

car.accelerate()
car.accelerate()
car.brake()

car.display()
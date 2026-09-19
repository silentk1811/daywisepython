class Temperature:
    
    def __init__(self):
        self.__celsius = 0

    def set_celsius(self, celsius):
        self.__celsius = celsius

    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

    def kelvin(self):
        return self.__celsius + 273.15


temperature = Temperature()

temperature.set_celsius(25)

print("Fahrenheit:", temperature.fahrenheit())
print("Kelvin:", temperature.kelvin())
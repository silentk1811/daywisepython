class Calculator:
    @staticmethod
    def square(n):
        return n * n

    @staticmethod
    def cube(n):
        return n * n * n

print(Calculator.square(4))
print(Calculator.cube(3))
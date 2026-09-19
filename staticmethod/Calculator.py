class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

print(Calculator.add(10, 5))
print(Calculator.sub(10, 5))
print(Calculator.mul(10, 5))
print(Calculator.div(10, 5))
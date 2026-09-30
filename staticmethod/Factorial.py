class Number:
    @staticmethod
    def factorial(n):
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact

    @staticmethod
    def sum_of_digits(n):
        total = 0
        while n > 0:
            total = total + n % 10
            n = n // 10
        return total

print(Number.factorial(5))
print(Number.sum_of_digits(123))
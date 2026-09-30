class Math:
    @staticmethod
    def check_even_odd(num):
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

Math.check_even_odd(7)
Math.check_even_odd(10)
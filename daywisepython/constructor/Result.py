class Result:
    def __init__(self, name, m1, m2, m3, m4, m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def result(self):
        total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        percentage = total / 5

        print("Total:", total)
        print("Percentage:", percentage)

        if percentage >= 40:
            print("Pass")
        else:
            print("Fail")

r = Result("Kalyani", 70, 80, 60, 75, 90)
r.result()
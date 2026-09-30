class Studentmarks:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def result(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        print("Total:", total)
        print("Percentage:", percentage)

s = Studentmarks("Kalyani", 80, 70, 90)
s.result()
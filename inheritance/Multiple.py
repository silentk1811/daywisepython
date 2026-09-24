class Father:
    def skill1(self):
        print("Father skill: Driving")

class Mother:
    def skill2(self):
        print("Mother skill: Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Child skill: Coding")

ch = Child()
ch.skill1()
ch.skill2()
ch.skill3()
class Person:
    
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        self.__age = age

    def check_vote(self):

        if self.__age >= 18:
            print("Eligible to vote")
        else:
            print("Not eligible to vote")


person = Person()

person.set_age(20)
person.check_vote()
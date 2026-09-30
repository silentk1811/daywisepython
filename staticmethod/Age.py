class AgeValidator:
    @staticmethod
    def can_vote(age):
        if age >= 18:
            print("Eligible to vote")
        else:
            print("Not eligible")

AgeValidator.can_vote(20)
AgeValidator.can_vote(16)
class Validator:
    @staticmethod
    def check_email(email):
        if "@" in email:
            print("Valid Email")
        else:
            print("Invalid Email")

Validator.check_email("kalyani@gmail.com")
Validator.check_email("kalyani.com")
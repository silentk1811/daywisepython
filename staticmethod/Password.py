class Password:
    @staticmethod
    def check_password(password):
        if len(password) >= 8:
            print("Valid Password")
        else:
            print("Password too short")

Password.check_password("abc12345")
Password.check_password("abc")
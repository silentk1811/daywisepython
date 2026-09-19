class Login:
    
    def __init__(self):
        self.__username = "kalyani"
        self.__password = "1234"

    def validate_login(self, username, password):

        if username == self.__username and password == self.__password:
            print("Login successful")
        else:
            print("Invalid username or password")


login = Login()

login.validate_login("kalyani", "1234")
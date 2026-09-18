class User:
    
    def __init__(self):
        self.__email = "kalyani@gmail.com"
        self.__password = "1234"

    def change_password(self, old_password, new_password):

        if old_password == self.__password:
            self.__password = new_password
            print("Password changed")
        else:
            print("Old password is incorrect")


user = User()

user.change_password("1234", "5678")
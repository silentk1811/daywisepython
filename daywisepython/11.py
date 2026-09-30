class LibraryBook:
    
    def __init__(self):
        self.__title = ""
        self.__issued = False

    def set_title(self, title):
        self.__title = title

    def issue_book(self):
        self.__issued = True
        print("Book issued")

    def return_book(self):
        self.__issued = False
        print("Book returned")

    def display_status(self):
        print("Book:", self.__title)

        if self.__issued:
            print("Status: Issued")
        else:
            print("Status: Available")


book = LibraryBook()

book.set_title("Python Programming")
book.issue_book()
book.display_status()

book.return_book()
book.display_status()
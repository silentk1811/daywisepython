class String:
    @staticmethod
    def reverse(s):
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        if s == s[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")

print(String.reverse("hello"))
String.is_palindrome("madam")
String.is_palindrome("python")
class Student:
    school_name = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

print("Old School:", Student.school_name)
Student.change_school("XYZ School")
print("New School:", Student.school_name)
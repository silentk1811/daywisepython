name = input("Enter student name: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()
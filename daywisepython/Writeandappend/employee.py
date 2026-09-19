file = open("employees.txt", "w")

for i in range(5):
    name = input("Enter employee name: ")
    file.write(name + "\n")

file.close()
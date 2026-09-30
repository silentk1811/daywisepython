file = open("numbers.txt", "w")

for i in range(5):
    number = input("Enter number: ")
    file.write(number + "\n")

file.close()
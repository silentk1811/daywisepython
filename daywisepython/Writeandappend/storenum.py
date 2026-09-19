file = open("numbers.txt", "w")

for i in range(1, 11):
    file.write(str(i) + "\n")

file.close()
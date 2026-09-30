file = open("messages.txt", "r")

for line in file:
    if "Python" in line:
        print(line)

file.close()
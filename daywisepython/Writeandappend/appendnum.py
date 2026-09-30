file = open("numbers.txt", "a")

for i in range(11, 21):
    file.write(str(i) + "\n")

file.close()
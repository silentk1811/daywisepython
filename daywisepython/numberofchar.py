file = open("messages.txt", "r")

data = file.read()
print("Number of characters:", len(data))

file.close()
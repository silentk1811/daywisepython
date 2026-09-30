file = open("messages.txt", "r")

data = file.read()

if "Hello" in data:
    print("Word exists")
else:
    print("Word does not exist")

file.close()
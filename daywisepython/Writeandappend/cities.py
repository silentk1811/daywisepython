file = open("cities.txt", "w")

file.write("Solapur\n")
file.write("Pune\n")
file.write("Mumbai\n")
file.write("Delhi\n")
file.write("Nashik\n")

file.close()

file = open("cities.txt", "a")

file.write("Nagpur\n")
file.write("Kolhapur\n")
file.write("Satara\n")

file.close()
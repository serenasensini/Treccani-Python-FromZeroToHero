# Leggere

myfile = open("test.txt")

open("test.txt", "w")

open("test.txt", "r")
open("test.txt")

open("test.txt", "wb")
myfile.close()

# Scrivere

file = open("test.txt", "r")
cont = file.read()
print(cont)
print(file.readlines())
file.close()

file = open("test.txt", "r")
cont = file.read()
print(cont)
for line in file:
    print(line)
file.close()

# Flusso completo

file = open("newfile.txt", "r")
print("Reading contents")
print(file.read())
file.close()

file = open("newfile.txt", "w")
file.write("Some bla bla bla")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
file.close()
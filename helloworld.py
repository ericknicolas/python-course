myfile = open("helloworld.txt")
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()

with open("helloworld.txt", mode="r") as myfile:
    print(myfile.read())

with open("helloworld.txt", mode="a") as myfile:
    print(myfile.write("\ntercera linea"))

with open("helloworld.txt", mode="r") as myfile:
    print(myfile.read())

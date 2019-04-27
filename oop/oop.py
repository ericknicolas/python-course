class Dog():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"

class Cat():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow!"

niko = Dog(name = "niko")
felix = Cat(name = "felix")

for pet in [niko,felix]:
    print(pet.speak())

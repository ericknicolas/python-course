class Dog():

    #Attributes
    breed = ""
    name  = ""
    sports = False

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name  = name
        self.spots = spots
    
    def bark(self):
        print("Woooof!")

    def print_name(self):
        print(f"My name is {self.name}")

my_dog = Dog(breed = "Lab", name = "White", spots = False)
print(my_dog.breed)
my_dog.bark()
my_dog.print_name()
class Animal():

    def __init__(self):
        print("animal created")
    
    def who_am_i(self):
        print("I'm an animal")

    def eat(self):
        print("I'm eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("dog created")
    
    def bark(self):
        print("wooof!")


my_dog = Dog()
my_dog.eat()
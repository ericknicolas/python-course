class Circle():

    #attributes
    pi = 3.14

    def __init__(self, radius = 1):
        
        self.radius = radius
    
    def get_circunference(self):
        return (2 * self.pi * self.radius)

circle = Circle(radius = 2)
print(circle.get_circunference())
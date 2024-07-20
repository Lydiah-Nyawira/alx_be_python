import math

# Define a base class Shape
class Shape:
    def __init__(self):
        pass
    
    def area(self):
    # This method is expected to be overridden in any subclass of Shape
        raise NotImplementedError

# Derived class - Rectangle   
class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):    
        return self.length * self.width

# Derived class -Circle   
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
# Program to calculate perimeter/circumference and area of a regular shape
import math

class RegularShape:
    def __init__(self, shape, side_length=None, radius=None, sides=None):
        self.shape = shape
        self.side_length = side_length
        self.radius = radius
        self.sides = sides
    
    def perimeter(self):
        if self.shape == "circle":
            return 2 * 3.14 * self.radius
        elif self.shape == "square":
            return 4 * self.side_length
        elif self.shape == "polygon":
            return self.sides * self.side_length
        else:
            return "Unknown shape"

    def area(self):
        if self.shape == "circle":
            return 3.14 * (self.radius ** 2)
        elif self.shape == "square":
            return self.side_length ** 2
        elif self.shape == "polygon":
            return (self.sides * self.side_length ** 2) / (4 * math.tan(math.pi / self.sides))
        else:
            return "Unknown shape"

# Example usage
circle = RegularShape("circle", radius=7)
square = RegularShape("square", side_length=5)
polygon = RegularShape("polygon", side_length=6, sides=5)

print("Circle Perimeter:", circle.perimeter())
print("Circle Area:", circle.area())
print("Square Perimeter:", square.perimeter())
print("Square Area:", square.area())
print("Polygon Perimeter:", polygon.perimeter())
print("Polygon Area:", polygon.area())

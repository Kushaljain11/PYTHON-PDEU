# Program to create a class that calculates surface area and volume of a solid
class Solid:
    def __init__(self, shape, radius=None, length=None, breadth=None, height=None):
        self.shape = shape
        self.radius = radius
        self.length = length
        self.breadth = breadth
        self.height = height
    
    def surface_area(self):
        if self.shape == "sphere":
            return 4 * 3.14 * (self.radius ** 2)
        elif self.shape == "cuboid":
            return 2 * (self.length * self.breadth + self.length * self.height + self.breadth * self.height)
        else:
            return "Unknown shape"

    def volume(self):
        if self.shape == "sphere":
            return (4/3) * 3.14 * (self.radius ** 3)
        elif self.shape == "cuboid":
            return self.length * self.breadth * self.height
        else:
            return "Unknown shape"

# Example usage
sphere = Solid("sphere", radius=5)
cuboid = Solid("cuboid", length=2, breadth=3, height=4)

print("Sphere Surface Area:", sphere.surface_area())
print("Sphere Volume:", sphere.volume())
print("Cuboid Surface Area:", cuboid.surface_area())
print("Cuboid Volume:", cuboid.volume())

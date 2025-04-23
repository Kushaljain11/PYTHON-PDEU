# Program to create Weather class and overload in operator
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

# Example usage
weather = Weather(["Sunny", "Cloudy", "Rainy", "Windy"])

print("Sunny in weather?", "Sunny" in weather)
print("Stormy in weather?", "Stormy" in weather)

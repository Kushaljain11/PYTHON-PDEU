# Program to implement String class with overloaded operators and methods
class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self

    def to_lower(self):
        self.value = self.value.lower()
        return self

    def to_upper(self):
        self.value = self.value.upper()
        return self

    def display(self):
        return self.value

# Example usage
s1 = String("Hello")
s1 += " World"
print("Concatenated String:", s1.display())

s1.to_lower()
print("Lowercase String:", s1.display())

s1.to_upper()
print("Uppercase String:", s1.display())

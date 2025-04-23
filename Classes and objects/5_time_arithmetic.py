# Program to create a Time class to perform time arithmetic operations
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)

    def subtract(self, other):
        total_seconds = self.to_seconds() - other.to_seconds()
        return Time.from_seconds(total_seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def display(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Example usage
t1 = Time(3, 45, 30)
t2 = Time(2, 20, 15)

print("Time 1:", t1.display())
print("Time 2:", t2.display())
print("Addition of Times:", (t1.add(t2)).display())
print("Subtraction of Times:", (t1.subtract(t2)).display())

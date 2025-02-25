import random

# Generate 10 random numbers in the range 15 to 45
numbers = {random.randint(15, 45) for _ in range(10)}

# Count how many numbers are less than 30
count_less_than_30 = sum(1 for number in numbers if number < 30)
print("Numbers less than 30:", count_less_than_30)

# Delete numbers greater than 35
numbers = {number for number in numbers if number <= 35}

# Display the updated set
print("Updated set:", numbers)

# 2.	Write a program to create a set containing 10 random numbers in the range 15 to 45. 
# Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.
import random
numbers = {random.randint(15, 45) for _ in range(10)}
print(numbers)
count_less_than_30 = sum(1 for number in numbers if number < 30)
print("Numbers less than 30:", count_less_than_30)
numbers = {number for number in numbers if number <= 35}
print("Updated set:", numbers)

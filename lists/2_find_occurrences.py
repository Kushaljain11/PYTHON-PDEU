# 2.	Generate 20 random integers and store them in a list. Accept a number from the user and print position of all occurrences of that number in the list.
import random

nums = [random.randint(1, 50) for _ in range(20)]
print("Generated List:", nums)

num = int(input("Enter a number to find positions: "))
positions = [i for i, x in enumerate(nums) if x == num]

if positions:
    print("Occurrences at positions:", positions)
else:
    print("Number not found")

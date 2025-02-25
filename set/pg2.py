import random
numbers = {random.randint(15, 45) for _ in range(10)}
print(numbers)
count_less_than_30 = sum(1 for number in numbers if number < 30)
print("Numbers less than 30:", count_less_than_30)
numbers = {number for number in numbers if number <= 35}
print("Updated set:", numbers)

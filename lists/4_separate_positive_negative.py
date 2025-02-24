import random

nums = [random.randint(-50, 50) for _ in range(30)]

positive_nums = [n for n in nums if n > 0]
negative_nums = [n for n in nums if n < 0]

print("Original List:", nums)
print("Positive Numbers:", positive_nums)
print("Negative Numbers:", negative_nums)

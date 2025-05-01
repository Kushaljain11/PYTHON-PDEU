# 4)	Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.
num = int(input("Enter a number: "))

# Prime check
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Perfect check
sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div += i
is_perfect = sum_div == num

# Armstrong check
order = len(str(num))
arm_sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    arm_sum += digit ** order
    temp //= 10
is_armstrong = arm_sum == num

# Palindrome check
s = str(num)
is_palindrome = s == s[::-1]

# Automorphic check
squared = num ** 2
is_automorphic = str(squared).endswith(str(num))

print(f"Prime: {is_prime}")
print(f"Perfect: {is_perfect}")
print(f"Armstrong: {is_armstrong}")
print(f"Palindrome: {is_palindrome}")
print(f"Automorphic: {is_automorphic}")

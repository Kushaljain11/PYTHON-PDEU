def to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)
num = int(input("Enter a positive integer: "))
print(f"Binary equivalent of {num} is: {to_binary(num)}")

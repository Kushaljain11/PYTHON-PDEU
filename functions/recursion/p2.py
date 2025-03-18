def to_binary(n):
    # Base case: when n is 0 or 1
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    
    # Recursive case: divide by 2 and concatenate the remainders
    return to_binary(n // 2) + str(n % 2)

# Example usage:
num = int(input("Enter a positive integer: "))
print(f"Binary equivalent of {num} is: {to_binary(num)}")

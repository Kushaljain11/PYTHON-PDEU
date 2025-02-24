s = input("Enter a string: ")
alphabets = 0
digits = 0

for char in s:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1

print(f"Alphabets: {alphabets}, Digits: {digits}")

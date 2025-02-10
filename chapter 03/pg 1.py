string = input("Enter a string: ")  # Accept input from user
vowels = "aeiouAEIOU"  # Define vowels
count = sum(1 for char in string if char in vowels)  # Count vowels

print("Number of vowels:", count)

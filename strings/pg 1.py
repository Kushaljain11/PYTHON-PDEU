# 1)	Count how many vowels are there in a string. Accept the string from the user.
string = input("Enter a string: ")  
vowels = "aeiouAEIOU"  
count = sum(1 for char in string if char in vowels)  

print("Number of vowels:", count)

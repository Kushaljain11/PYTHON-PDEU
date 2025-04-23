# 4. Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.
string = input()
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)

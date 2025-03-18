def count_vowels(s):
    if not s:
        return 0
    vowels = "aeiouAEIOU"
    if s[0] in vowels:
        return 1 + count_vowels(s[1:])
    return count_vowels(s[1:])
string = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(string)}")

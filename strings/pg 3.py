def is_substring(s1, s2):
    for i in range(len(s1) - len(s2) + 1):
        if s1[i:i+len(s2)] == s2:
            return True
    return False

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if is_substring(s1, s2):
    print("Yes, the second string is in the first string.")
else:
    print("No, the second string is not in the first string.")


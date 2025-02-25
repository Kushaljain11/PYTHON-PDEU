
def is_substring(str1, str2):
    if str2 in str1:
        return True
    else:
        return False
    
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if is_substring(string1, string2):
    print(f"'{string2}' is present in '{string1}'")
else:
    print(f"'{string2}' is not present in '{string1}'")

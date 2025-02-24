#2)Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case
def to_lowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char  # Keep lowercase and other characters unchanged
    return result

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result += chr(ord(char) - 32)
        else:
            result += char  # Keep uppercase and other characters unchanged
    return result

def toggle_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result += chr(ord(char) - 32)
        else:
            result += char  # Keep other characters unchanged
    return result

# Test the functions
string = input("Enter a string: ")
print("Lowercase:", to_lowercase(string))
print("Uppercase:", to_uppercase(string))
print("Toggle Case:", toggle_case(string))

    

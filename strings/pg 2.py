
def to_lowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32)
        else:
            result += char  
    return result

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z': 
            result += chr(ord(char) - 32)
        else:
            result += char 
    return result

def toggle_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z': 
            result += chr(ord(char) - 32)
        else:
            result += char 
    return result


string = input("Enter a string: ")
print("Lowercase:", to_lowercase(string))
print("Uppercase:", to_uppercase(string))
print("Toggle Case:", toggle_case(string))

    

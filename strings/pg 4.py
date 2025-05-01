# ''' 4)	Write a function that removes one string from another string, if present.
#  E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef”.'''
def remove_substring(s, sub):
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(sub)] == sub:
            i += len(sub)
        else:
            result += s[i]
            i += 1
    return result

s = input("Enter the main string: ")
sub = input("Enter the string to remove: ")

print("Final string:", remove_substring(s, sub))

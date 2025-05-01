# ''' 4)	Write a function that removes one string from another string, if present.
#  E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef”.'''
st1 = input("Enter string: ")
remSt = input("Remove string: ")

print(st1.replace(remSt, ""))

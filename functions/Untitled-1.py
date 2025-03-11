""""1)Write a program that defines a function count_lower_upper() that accepts a string and calculates
the number of uppercase and lowercase alphabets in it. It should return these values as a dictionary.
Call this function for some sample string."""
def count_lower_upper():
    str=input("enter a string:")
    d = {'uppercase':0,'lowercase':0}
    for i in str:    
        if i.isupper():
            d["uppercase"]+=1
        if i.islower():
            d["lowercase"]+=1
    print(d)
count_lower_upper()

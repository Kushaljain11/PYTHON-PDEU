"""Write a function to create and return a list containing tuples of the form (x,x2,x3) for all x between 1 and given ending value (both inclusive)."""
def generate_tuples(end_value):
    result = []
    for x in range(end_value):
        result.append((end_value, end_value**2, end_value**3))
        return result  

print(generate_tuples(5))

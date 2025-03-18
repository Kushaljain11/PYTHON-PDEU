def count_alpha_digits(s):
    count = {'alphabets': 0, 'digits': 0}
    
    for char in s:
        if char.isalpha():
            count['alphabets'] += 1
        elif char.isdigit():
            count['digits'] += 1
    
    return count


text = "Hello 123 World!"
print(count_alpha_digits(text))  

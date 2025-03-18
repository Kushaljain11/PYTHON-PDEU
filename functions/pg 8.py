def convert(s):
    
    words = s.split()
    
    unique_words = sorted(set(words))
    
    return " ".join(unique_words)


sentence = "apple banana apple grape banana orange"
print(convert(sentence))  

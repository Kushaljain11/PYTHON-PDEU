def frequency(s):
    words = s.split()
    freq = {}
    
    for word in words:
        word = word.lower()  
        freq[word] = freq.get(word, 0) + 1
    
    
    sorted_freq = sorted(freq.items())
    
    return sorted_freq


sentence = "Hello world hello Python world"
print(frequency(sentence))  

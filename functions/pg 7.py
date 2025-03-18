def ispalindrome(s):
    
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]
word = "A man a plan a canal Panama"
print(ispalindrome(word))  


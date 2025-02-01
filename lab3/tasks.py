# first task

def ounces(grams):
    return grams * 28.3495231

print(ounces(100))

# eleventh task

def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(palindrome("madam")) 
print(palindrome("hello")) 
print(palindrome("racecar")) 
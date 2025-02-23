import re

def find_upper_followed_by_lower(s):
    return re.findall(r'[A-Z][a-z]+', s)

print(find_upper_followed_by_lower("Hello World Python")) 
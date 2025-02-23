import re

def replace_space_comma_dot(s):
    return re.sub(r'[ ,.]', ':', s)

print(replace_space_comma_dot("Hello, world. How are you?")) 
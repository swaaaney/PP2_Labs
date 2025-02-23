import re

def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

print(split_at_uppercase("HelloWorldPython")) 
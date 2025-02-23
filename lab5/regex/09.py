import re

def insert_spaces_capitals(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

print(insert_spaces_capitals("HelloWorldPython"))
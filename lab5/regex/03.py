import re

def find_lowercase_underscore(s):
    return re.findall(r'[a-z]+_[a-z]+', s)

print(find_lowercase_underscore("hello_world this_is_test")) 
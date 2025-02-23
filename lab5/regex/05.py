import re

def match_a_anything_b(s):
    return bool(re.fullmatch(r'a.*b', s))

print(match_a_anything_b("acb"))   
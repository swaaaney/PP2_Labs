import re

def match_a_two_to_three_b(s):
    return bool(re.fullmatch(r'ab{2,3}', s))

print(match_a_two_to_three_b("abb"))
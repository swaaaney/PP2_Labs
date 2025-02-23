import re
def match_ab_zero_or_more_b(s):
    return bool(re.fullmatch(r'ab*', s))


print(match_ab_zero_or_more_b("abbb"))
import os
import time
import shutil
import math
import string

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower
print(count_case("Hello World!"))
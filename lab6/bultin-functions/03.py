import os
import time
import shutil
import math
import string

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("qwerty"))
print(is_palindrome("abba"))
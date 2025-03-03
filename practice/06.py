import math

def sqrt_floor(num):
    return math.sqrt(num)

print(sqrt_floor(20))

import re

text = "Hello 123 world"
match = re.findall(r"\d+", text)
print(match)

text = "My number is 12345"
new_text = re.sub(r"\d", "*", text)
print(new_text)

text = "Contact me at akku.yermankyzy@bk.ru or a_yermankyzy@kbtu.kz"
emails = re.findall(r"[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)

def find_numbers(text):
    return re.findall(r"\d+", text)
print(find_numbers("I have 2 apples and 35 bananas."))

def math_operations(nums):
    return(math.sqrt(nums), math.ceil(nums), math.floor(nums))
print(math_operations(10.7))

def is_valid_email(text):
    if re.findall(r"[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text):
        return "True"
    else:
        return "False"
print(is_valid_email("akku.yermankyzy@bk.ru"))
print(is_valid_email("hello world"))

def word(text):
    return (re.findall(r"\d+", text))
print(word("Hello 1234 you"))
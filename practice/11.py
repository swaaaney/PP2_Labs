from datetime import datetime

# first task

current = datetime.now()
print(current)

# second card

def generators():
    n = 1
    while True:
        yield n**2
        n += 1
gen = generators()
for _ in range(5):
    print(next(gen))

# third task

import json

def write_json():
    data = {
        "name" : "Jean",
        "age" : 17,
        "city": "Paris"
    }
    with open("data.json", "w") as file:
        json.dump(data, file)
write_json()

def read_json():
    with open("data.json", "r") as file:
        return json.load(file)

print(read_json())

# fourth task

import math

def math_operations(nums):
    total = sum(nums)
    avg = total/len(nums)
    math_sqrt = math.sqrt(max(nums))
    return total, avg, math_sqrt
print(math_operations([1, 2, 3, 4, 5]))

# fifth task

import re

def is_number(text: str):
    return bool(re.fullmatch(r"^\+?[0-9]{10,15}$", text))
 
print(is_number("+77771234567"))

# sixth task

import os
def create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)
    else:
        print("this folder is aalready exists")
create_dir("backup")

def create_file(dir, filename):
    path = os.path.join(dir, filename)
    with open(path, "w") as file:
        file.write("Hello, world!")

my_fold = "backup"
create_file(my_fold, "data.txt")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

def first_uppercase(text):
    """Возвращает первую заглавную букву из строки"""
    for char in text:
        if char.isupper():
            return char
    return None  # Если заглавных букв нет

print(first_uppercase("hello World"))  # ➝ 'W'
print(first_uppercase("python"))       # ➝ None
print(first_uppercase("I love You"))   # ➝ 'I'
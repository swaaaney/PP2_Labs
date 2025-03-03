import math
# Math

# first task
def pow(number):
    return math.sqrt(number)
print(pow(144))

# second task
def rounded(number):
    return math.ceil(number)
print(rounded(5.8))

# third task
def sinus(numbers):
    return math.sin(numbers)
print(sinus(30))

import re
# Regex

#first task
def allnums(text):
    return re.findall(r"\d+", text)
print(allnums("My number is 2024, his is 777 and hers is 12345"))

# second task
def email(text):
    if re.findall(r"[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text):
        return True
    else:
        return False
print(email("Hello this is my main email: a_yermankyzy@kbtu.kz"))

# third task
def task(text):
    return re.sub(r"\s", "_", text)
print(task("Hello world, how are you?"))

import os
# dir and files

#first task
def new_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)
        print(f"New folder {name} is available now!")
    else:
        print(f"This folder {name} already exists!")
new_folder("test_folder")

# second task
def new_file():
    with open("hello.txt", "w") as file:
        return file.write("Hello, Alex!")
new_file()

# third task
def read_file():
    with open("hello.txt", "r") as file:
        return file.read()
print(read_file())

# fourth task
def delete_file(name):
    if os.path.exists(name):
        os.remove(name)
    else:
        print(f"File {name} doesnt exists!")
delete_file("ponti.txt")
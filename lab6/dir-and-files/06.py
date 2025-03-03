import os
import time
import shutil
import math
import string

import string

import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as file:
            file.write(f"File {letter}") 

generate_text_files() 
import os
import time
import shutil
import math
import string

def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)
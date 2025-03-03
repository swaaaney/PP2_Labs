import os
import time
import shutil
import math
import string

import os

def count_lines(file_path):
    if not os.path.exists(file_path):
        return f"Error: File '{file_path}' not found."
    
    with open(file_path, 'r') as f:
        return sum(1 for _ in f)

print(count_lines("test.txt")) 
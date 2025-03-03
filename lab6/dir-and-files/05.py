import os
import time
import shutil
import math
import string

def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(str(item) + "\n")
write_list_to_file("output.txt", ["apple", "banana", "cherry"])
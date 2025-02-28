import os
import time
import shutil
import math
import string

def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        file.writelines(f"{item}\n" for item in data_list)

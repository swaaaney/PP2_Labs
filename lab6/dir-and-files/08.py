import os
import time
import shutil
import math
import string

def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    else:
        print("Cannot delete, no access or file does not exist.")

import os
import time
import shutil
import math
import string

import os

def path_info(path):
    if os.path.exists(path):
        return {"Directory": os.path.dirname(path), "Filename": os.path.basename(path)}
    return "Path does not exist"

print(path_info("test_folder/test.txt"))
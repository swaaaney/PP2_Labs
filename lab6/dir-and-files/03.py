import os
import time
import shutil
import math
import string

def path_info(path):
    if os.path.exists(path):
        return os.path.dirname(path), os.path.basename(path)
    return None

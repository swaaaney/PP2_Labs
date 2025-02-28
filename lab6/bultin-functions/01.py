import os
import time
import shutil
import math
import string

from functools import reduce
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

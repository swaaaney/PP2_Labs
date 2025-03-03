import os
import time
import shutil
import math
import string

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")
    
delayed_sqrt(25100, 2123)
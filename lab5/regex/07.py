import re

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    return ''.join(word.capitalize() for word in words)

print(snake_to_camel("hello_world_test")) 
import os

def new_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)
        print(f"new folder {name} is here")
    else:
        print(f"new folder {name} is already exists")
new_folder("test.txt")

def delete_folder(name):
    if os.path.exists(name):
        os.rmdir(name)
        print(f"folder {name} is deleted")
    else:
        print(f"folder {name} does not exist")
delete_folder("test.txt")

def delete_file(name):
    if os.path.exists(name):
        os.remove(name)
        print(f"file {name} is deleted")
    else:
        print(f"file {name} does not exist")
delete_file("Z.txt")


import os

# first task
def new_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)
        print(f"Creating new file {name} is ready!")
    else:
        print(f"The folder {name} is already exists!")
new_folder("my_folder")

# second task
def create_file():
    with open("numbers.txt", "w") as file:
        numbers = " ".join(map(str, range(1, 11)))
        file.write(numbers)
        print(f"New file with numbers from 1 to 10")
create_file()

# third task
def read_file():
    with open("numbers.txt", "r") as file:
        numbers = list(map(int, file.read().split()))
        return sum(numbers)
print((read_file()))

# fourth task
def rename_file():
    if os.path.exists("numbers.txt"):
        os.rename("numbers.txt", "data.txt")
        print(f"file renamed to 'data.txt' ")
    else:
        print(f"file 'numbers.txt' does not exists")
rename_file()

# fifth task
def list_directory():
    return os.listdir(".")
print(f"current directory files and folders: {list_directory()}")

# sixth task
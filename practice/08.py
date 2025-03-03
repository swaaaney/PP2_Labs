import os

def create_and_write_file():
    with open("test.txt", "w") as file:  
        file.write("Hello, world!")
    print("Файл 'test.txt' создан и записан!")

create_and_write_file()


def read_file():
    try:
        with open("test.txt", "r") as file: 
            return file.read()
    except FileNotFoundError:
        return "Файл не найден!"

print(read_file())

def delete_file():
    if os.path.exists("test.txt"):
        os.remove("test.txt")
        print("Файл 'test.txt' удалён!")
    else:
        print("Файл 'test.txt' не существует!")

delete_file()
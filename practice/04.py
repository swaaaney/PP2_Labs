def generator():
    for i in range(1, 6):
        yield i

gen = generator()
for number in gen:
    print(number)
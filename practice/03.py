# first task

text = "hello, world!"
print(text.upper())

#second task

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num:
    if i % 2 == 0:
        print(i)
#third task

n = int(input("enter your number: "))
if n % 2  == 0:
    print(f"Your number {n} is even!")
else:
    print(f"Your number {n} is odd!")

#fourth task

person = {
    "Jean": 17,
    "Alex": 18,
    "Donut":7
}
person["Tolstoy"] = 9
print(person["Tolstoy"])

#fifth task

numbers = [3, 5, 7, 9]
total = sum(numbers)
print(total)

#sixth task

with open("data.txt", "w") as file:
    file.write("Hello, Alex!")
with open("data.txt", "r") as file:
    print(file.read())

# seventh task
for i in range(10, 0, -1):
    print(i)

# eigth task

def avg(num):
    total = sum(num) 
    return total / len(num)

my_average = [1, 2, 3, 4, 5]
print(avg(my_average)) 

# ninth task

palindrom = str(input())
rev =  palindrom[::-1]
if(palindrom == rev):
    print(f"Yes, {palindrom} is palindrom")
else:
    print(f"No, {palindrom} isn't palindrom")

# tenth task

num = [111, 233, 32, -2, 50, 61, 7, 2]
print(max(num))

# eleventh task

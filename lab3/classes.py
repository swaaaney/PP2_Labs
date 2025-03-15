# first task

class YourWord:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Your word: ")

    def printString(self):
        print(self.string.upper())

word = YourWord()
word.getString()
word.printString()

# second task

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length **2
    
square = Square(67)
print(f"The area of the square is: {square.area()}")

# third task

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

rectangle = Rectangle(6, 7)
print(f"The area of the recktangle is: {rectangle.area()}")

# fourth task

import math 

class Point:
    def __init__(self, num1 = 0, num2 = 0): 
        self.num1 = num1
        self.num2 = num2

    def show(self):
        print(f"Point({self.num1}, {self.num2})")

    def move(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def dist(self, other): 
        return math.sqrt((self.num1 - other.num1) ** 2 + (self.num2 - other.num2) ** 2)

point1 = Point(1, 2) 
point2 = Point(4, 6)

point1.show() 
point2.show() 

point1.move(3, 3)
point1.show() 

distance = point1.dist(point2)  
print(f"The distance between the two points is: {distance:.2f}")  

# fifth task

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
    
my_account = Account("John", 100)
my_account.deposit(50)
print(my_account.get_balance())

# sixth task

from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", primes)
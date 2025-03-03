# first task

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says wolf!")

my_dog = Dog("Rex", 5)
print(my_dog.age)
my_dog.bark()

# second task

class Recktangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def perimetr(self):
        return  2*(self.width + self.height)

my_reck = Recktangle(3, 5)
print(f"area is equal to {my_reck.area()}")
print(f"perimetr is equal to {my_reck.perimetr()}")

# third task

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

#fourth task
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def substract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        elif self.num1 == 0:
            print(f"the answer is {self.num1}!")
        elif self.num2 == 0:
            print(f"we can't divide numbers to {self.num2}!")

my_calc = Calculator(10, 0)
print(my_calc.add())
print(my_calc.substract())
print(my_calc.multiply())
print(my_calc.divide())

# fifth task
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def add_seconds(self, sec):
        self.second += sec
        if self.second >= 60:
            self.minute += (self.second // 60)
            self.second %= 60
            if self.minute >= 60:
                self.hour += (self.minute // 60)
                self.minute %= 60

    def get_time(self):
        return(f"{self.hour:02}:{self.minute:02}:{self.second:02}")

time = Time(12, 30, 45)
time.add_seconds(2000)
print(time.get_time())

# sixth task

class Animals:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def alive(self):
        if self.family == "Dinosaur":
            return (f"this animal is extinct, sorry")
        else:
            return (f"this animal is alive")
        
my_animal = Animals("golden retriever", "dog")
print(my_animal.alive())

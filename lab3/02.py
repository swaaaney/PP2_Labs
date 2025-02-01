# first task

def ounces(grams):
    return grams * 28.3495231

print(ounces(100))

# second task

def Fahrenheit(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

print(Fahrenheit(100))

# third task

def solve(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if (2 * chickens + 4 * rabbits) == legs:
            return chickens, rabbits

print(solve(35, 94))

# fourth task

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if prime(num)]

print(filter_prime([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

# fifth task

from itertools import permutations

def string(s):
    return [''.join(p) for p in permutations(s)]

print(string("abc"))

# sixth task

def reverse(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse("We are ready"))

#seventh task

def has_33(num):
    for i in range(len(num) - 1):
        if num[i] == 3 and num[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3])) 
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3])) 

#eigth task

def game(n):
    code = [0, 0, 7]
    for num in n:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(game([1, 2, 4, 0, 0, 7, 5])) 
print(game([1, 0, 2, 4, 0, 5, 7])) 
print(game([1, 7, 2, 0, 4, 5, 0]))

#ninth task

import math

def sphere(radius):
    return (4/3) * math.pi * radius**3

print(sphere(3))

# tenth task

def unique(l):
    new_list = []
    for num in l:
        if num not in new_list:
            new_list.append(num)
    return new_list

print(unique([1, 2, 2, 3, 4, 4, 5]))

# eleventh task

def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(palindrome("madam")) 
print(palindrome("hello")) 
print(palindrome("racecar")) 

# twelveth task

def histogram(l):
    for num in l:
        print('*' * num)

histogram([4, 9, 7])

# thirtinth task

import random

def guess_number():
    name = input("Hello! What is your name? ")
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    attempts = 0
    while True:
        guess = int(input("\nTake a guess: "))
        attempts += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

# fourtith task

from tasks import ounces, palindrome

print(ounces(100))
print(palindrome("madam")) 
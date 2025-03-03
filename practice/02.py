# FUNCTIONS 
#first task

def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(1000)) 

# second task

def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

print(fahrenheit_to_celsius(120))

# third task

def solve(numheads, numlegs):
    for chikens in range(numheads + 1):
        rabbits = numheads - chikens
        if(2 * chikens + 4 * rabbits) == numlegs:
            return chikens, rabbits
        
print(solve(35, 94))

# fourth task

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % 2 == 0:
            return False
    return True
def filter_prime(numbers):
    return [ num for num in numbers if prime(num)]
print(filter_prime([1, 2, 3, 4, 5, 6]))
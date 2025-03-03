#first task

def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers)/len(numbers)
    return(minimum, maximum, average)
print(stats([3, 5, 7, 9]))

#second task

def sum_even(numbers):
    return sum(num for num in numbers if num % 2 == 0)
print(sum_even([1, 2, 3, 4, 5, 6]))
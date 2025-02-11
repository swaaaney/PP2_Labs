def generate_squares(n):
    for i in range(n + 1):
        yield i ** 2

# Example usage
n = 5
for square in generate_squares(n):
    print(square)
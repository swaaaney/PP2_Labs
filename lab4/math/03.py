import math

num_sides = 4
side_length = 25

area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

print(f"Input number of sides: {num_sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {area:.2f}")
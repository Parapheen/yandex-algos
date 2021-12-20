import math

d = int(input())
x, y = map(int, input().split())

def count_dst(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def count_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

if x >= 0 and y >= 0 and x + y <= d:
    print(0)
else:
    x_to_a = count_dst(0, x, 0, y)
    x_to_b = count_dst(d, x, 0, y)
    x_to_c = count_dst(0, x, d, y)
    if x_to_a <= x_to_b and x_to_a <= x_to_c:
        print(1)
    elif x_to_b <= x_to_a and x_to_b <= x_to_c:
        print(2)
    elif x_to_c <= x_to_a and x_to_c <= x_to_b:
        print(3)
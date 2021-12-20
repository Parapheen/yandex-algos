x, y, z = map(int, input().split())
is_obvious = 0

if (x <= 12 and y > 12) or (x > 12 and y <= 12) or (x == y):
    is_obvious = 1

print(is_obvious)
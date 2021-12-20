a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

print(len(a) - len(set(a) - set(b)))
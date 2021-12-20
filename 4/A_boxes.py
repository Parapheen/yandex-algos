boxes = int(input())
values = [[int(i) for i in input().split()] for _ in range(boxes)]

res = {}
for box in values:
    if not box[0] in res:
        res[box[0]] = 0
    res[box[0]] += box[1]
for color in sorted(res):
    print(color, res[color])
res = {}
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        inp = line.split()
        name = inp[0]
        votes = int(inp[1])
        if name not in res:
            res[name] = votes
        else:
            res[name] += votes
for name in sorted(res):
    print(name, res[name])
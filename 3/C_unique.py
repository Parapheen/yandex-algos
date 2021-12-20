a = [int(i) for i in input().split()]

dct = {}
for i in a:
	if i not in dct:
		dct[i] = 1
	else:
		dct[i] += 1
res = [i for i in dct if dct[i] == 1]
print(*res)

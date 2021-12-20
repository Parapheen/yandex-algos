a = [int(i) for i in input().split()]

seen = set()
for i in a:
	if i not in seen:
		seen.add(i)
		print('NO')
	else:
		print('YES')
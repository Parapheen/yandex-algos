total_folders = int(input())
diplomas = [int(a) for a in input().split()]

res = 0
max_diplomas = diplomas[0]
for i in diplomas:
	res += i
	if i > max_diplomas:
		max_diplomas = i
print(res - max_diplomas)
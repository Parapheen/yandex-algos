import math

l, k = map(int, input().split())
dst = list(map(int, input().split()))

mid = math.floor(l / 2)
last_leg = 0
for i in range(k):
	if dst[i] < mid:
		last_leg = i
	elif dst[i] == mid:
		if l % 2 != 0:
			print(dst[i])
			break
		else:
			print(dst[last_leg], dst[i])
			break
	else:
		print(dst[last_leg], dst[i])
		break


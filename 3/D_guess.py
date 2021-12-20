max_nbr = int(input())

possible = set(range(1, max_nbr + 1))

while True:
	inp = input()
	if inp == 'HELP':
		break
	guess = set(int(i) for i in inp.split())
	ans = input()
	if ans == 'YES':
		possible.intersection_update(guess)
	elif ans == 'NO':
		possible.difference_update(guess)

print(*sorted(possible))

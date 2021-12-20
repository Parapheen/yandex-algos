
def read_nbrs():
    nbrs = []
    while True:
        nbr = int(input())
        if (nbr == 0):
            break
        nbrs.append(nbr)
    return nbrs

nbrs = sorted(read_nbrs())
max_nbr = nbrs[-1]
i = len(nbrs) - 1
res_counter = 0
while i >= 0 and nbrs[i] == nbrs[-1]:
    res_counter += 1
    i -= 1
print(res_counter)
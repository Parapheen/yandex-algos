n, q = map(int, input().split())
nbrs = [int(i) for i in input().split()]

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nbrs[i - 1]

for i in range(q):
    l, r = map(int, input().split())
    print(prefix_sum[r] - prefix_sum[l - 1])

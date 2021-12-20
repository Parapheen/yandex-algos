n = int(input())
nbrs = [int(i) for i in input().split()]

prefix_sum = [0] * (n + 1)
max_sum = 0
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nbrs[i - 1]
    if prefix_sum[i] > max_sum:
        max_sum = prefix_sum[i]

print(prefix_sum)
print(max_sum)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = arr[i - 1] + prefix_sum[i - 1]

for _ in range(m):
    i, j = map(int, input().split())

    print(prefix_sum[j] - prefix_sum[i - 1])

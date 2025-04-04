import sys
input = sys.stdin.readline
n, m = map(int, input().split())

ary = [list(map(int, input().split())) for i in range(n)]
# print(ary)
dp = [[0]*(m+1) for _ in range(n+1)]
# print(dp)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = ary[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
# print(dp)

c = int(input())
for _ in range(c):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
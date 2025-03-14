import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 2-친구 사이일 때 1, 아니면 0
f = [[0] * n for _ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      # 2-친구인 경우
      if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
        f[i][j] = 1

res = 0

for row in f:
  res = max(res,sum(row))
print(res)
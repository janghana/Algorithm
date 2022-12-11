import sys

N, M = map(int, input().split())

graph = {}
s = [[100] * N for i in range(N)]

for i in range(M):
    a, b, cost = map(int, input().split())
    s[a][b] = cost

for k in range(0, N):
    for i in range(0, N):
        for j in range(0, N):
            if i == j:
                s[i][j] = 0
            if s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]

for i in s:
    result = 0
    for j in i:
        result += j
    print(result)

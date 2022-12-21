import sys
INF = sys.maxsize

N, M = map(int, input().split())

s = [[INF] * N for i in range(N)]
for i in range(M):
    num1, num2 = map(int, input().split())
    s[num1 - 1][num2 - 1] = 1
    s[num2 - 1][num1 - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            s[i][j] = min(s[i][j], s[i][k]+s[k][j])

result = sys.maxsize
for i in range(N):
    sum = 0
    for j in range(N):
        sum += s[i][j]
    if result > sum:
        result = sum
        p = i
print(p + 1)

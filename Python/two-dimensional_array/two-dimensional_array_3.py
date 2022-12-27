N = int(input())

src = [[0]*101 for _ in range(101)]
result = 0
for _ in range(N):
    x, y = map(int ,input().split())
    for i in range(10):
        for j in range(10):
            src[x+i][y+j] = 1

for i in src:
    for j in i:
        if j == 1:
            result += 1
print(result)

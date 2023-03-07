N, M = map(int, input().split())
li = [0]*(N+1)
for _ in range(M):
    i,j,k = map(int, input().split())
    for p in range(i,j+1):
        li[p] = k
li.remove(li[0])
print(*li)

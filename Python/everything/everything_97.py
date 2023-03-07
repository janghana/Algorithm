N, M = map(int, input().split())
li = [i for i in range(N+1)]
for _ in range(M):
    i,j = map(int, input().split())
    tmp = li[j]
    li[j] = li[i]
    li[i] = tmp
li.remove(li[0])
print(*li)

N, M = map(int ,input().split())
result = []
visited = [False]*(N+1)

def DFS():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        visited[i] = True
        result.append(i)
        DFS()
        result.pop()
        visited[i] = False
DFS()

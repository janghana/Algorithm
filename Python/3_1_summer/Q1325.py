from collections import deque
import sys

r = sys.stdin.readline

N, M = map(int, r().split())

array = [[] for _ in range(N + 1)]


def bfs(v):
    q = deque([v])
    visited = [False] * (N + 1)
    visited[v] = True
    cnt = 1
    while q:
        v = q.popleft()
        for node in array[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                cnt += 1

    return cnt


for _ in range(M):
    a, b = map(int, r().split())
    array[b].append(a)

results = []
max_value = -1
for i in range(1, N + 1):
    result = bfs(i)
    if result > max_value:
        results = [i]
        max_value = result
    elif result == max_value:
        results.append(i)

for re in results:
    print(re, end=" ")

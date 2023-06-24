from sys import stdin
from collections import deque

V = int(stdin.readline())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    C = list(map(int, stdin.readline().split()))
    for e in range(1, len(C) - 2, 2):
        graph[C[0]].append((C[e], C[e + 1]))


def bfs(start):
    visit = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e

    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)

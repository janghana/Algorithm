import sys


def bellmanford(graph, V, E, start):
    distance = {}
    for i in node_list:
        distance[i] = sys.maxsize
    distance[start] = 0

    for _ in range(V - 1):
        for n in graph:
            for k in range(len(graph[n])):
                if distance[n] != sys.maxsize and distance[graph[n][k][0]] > distance[n] + graph[n][k][1]:
                    distance[graph[n][k][0]] = distance[n] + graph[n][k][1]
                    prev[graph[n][k][0]] = [n, graph[n][k][1]]

    nCycle = False
    for n in graph:
        if len(graph[n]) == 0:
            continue
        if distance[graph[n][0][0]] > distance[n] + graph[n][0][1]:
            nCycle = True
    if nCycle:
        print("Negative")
    return nCycle


V, E = map(int, input().split())
start, end = map(str, input().split())
node_list = list(map(str, input().split()))
prev = {}
graph = {}
for i in node_list:
    prev[i] = []
    graph[i] = []
for i in range(E):
    a, b, cost = map(str, input().split())
    graph[a].append([b, int(cost)])

nCycle = bellmanford(graph, V, E, start)

if not nCycle:
    visit = []
    cur = end
    while cur in prev and cur != start:
        visit.append([prev[cur][0], cur, prev[cur][1]])
        cur = prev[cur][0]

    for tmp in reversed(visit):
        print(*tmp)

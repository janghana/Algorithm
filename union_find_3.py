import sys

sys.setrecursionlimit(10 ** 6)


def find_parent(node):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent[node])
    return parent[node]


def union(node1, node2):
    node1 = find_parent(node1)
    node2 = find_parent(node2)
    print(rank)

    if rank[node1] > rank[node2]:
        parent[node2] = node1
    else:
        parent[node1] = node2
        if parent[node1] == parent[node2]:
            node2 += 1


def kruskal(edges):
    edges.sort()

    total = 0
    MST = []

    for edge in edges:
        cost, node1, node2 = edge
        if find_parent(node1) != find_parent(node2):
            union(node1, node2)
            total += cost
            MST.append([node1, node2])

    return total, MST


N, M = map(int, input().split())
satelite_list = list(map(int, input().split()))
parent = [i for i in range(M + N)]
rank = [[] for i in range(M + N)]
edges = [[] for i in range(M + N)]

k = 0
j = 1
for i in satelite_list:
    edges[k].extend([i, 0, j])
    j += 1
    k += 1

for i in range(k, M + k):
    town1, town2, cost = map(int, input().split())
    edges[i].extend([cost, town1, town2])

total, mst = kruskal(edges)
print(total)

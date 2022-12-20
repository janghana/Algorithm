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

    if rank[node1] > rank[node2]:
        parent[node2] = node1
    else:
        parent[node1] = node2
        if parent[node1] == parent[node2]:
            node2 += 1


def kruskal(edges):
    edges.sort()

    total_cost = 0
    MST = []

    for edge in edges:
        cost, node1, node2 = edge

        if find_parent(node1) != find_parent(node2):
            union(node1, node2)
            total_cost += cost
            MST.append([node1, node2])
    return total_cost, MST


N, M = map(int, input().split())
Node_list = list(map(str, input().split()))

parent = [i for i in range(M)]
rank = [[] for i in range(M)]
edges = [[] for i in range(M)]

for i in range(M):
    node1, node2, cost = map(str, input().split())
    tmp_node1 = 0
    tmp_node2 = 0
    for j in range(len(Node_list)):
        if node1 == Node_list[j]:
            tmp_node1 = j
    for j in range(len(Node_list)):
        if node2 == Node_list[j]:
            tmp_node2 = j
    edges[i].extend([int(cost), tmp_node1, tmp_node2])

total_cost, MST = kruskal(edges)

cost_list = []

for i in MST:
    new_edges = []
    parent = [i for i in range(M)]
    rank = [[] for i in range(M)]
    for edge in edges:
        cost, node1, node2 = edge
        if [node1, node2] == i:
            continue
        else:
            new_edges.append(edge)

    tmp_cost, tmp_mst = kruskal(new_edges)
    cost_list.append(tmp_cost)

cost_list.sort()
print(cost_list[0])

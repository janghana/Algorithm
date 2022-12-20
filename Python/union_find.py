import sys
sys.setrecursionlimit(10 ** 6)

def find_parent(a):
    if parent[a] == a:
        return a
    parent[a] = find_parent(parent[a])
    return parent[a]

def union_set(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b :
        return
    if rank[a] > rank[b]:
        parent[b] = a
    else :
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

def kruskal(edges):
    edges.sort()
    total_cost = 0
    MST = []

    for edge in edges:
        cost, node1, node2 = edge
        if find_parent(node1) != find_parent(node2):
            union_set(node1, node2)
            total_cost += cost
            MST.append((node1, node2))
    return total_cost, MST


# def getParent(parent, x):
#     if parent[x] == x:
#         return x
#     parent[x] = getParent(parent, parent[x])
#     return parent[x]
#
# def unionParent(parent, a, b):
#     a = getParent(parent, a)
#     b = getParent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# def findParent(parent, a, b):
#     a = getParent(parent, a)
#     b = getParent(parent, b)
#     if a == b:
#         return True
#     else:
#         return False



N, M = map(int, input().split())
NODE_LIST = list(map(str, input().split()))
parent = [0] * (N + 1)
rank = [0] * (N + 1)
parent = [i for i in range(N)]
edges = [[] for i in range(M)]

for i in range(M):
    node1, node2, cost = map(str, input().split())
    tmp_a = 0
    tmp_b = 0
    for j in range(0,len(NODE_LIST)):
        if NODE_LIST[j] == node1:
            tmp_a = j
    for j in range(0,len(NODE_LIST)):
        if NODE_LIST[j] == node2:
            tmp_b = j

    print(node1, node2, tmp_a, tmp_b)
    edges[i].extend([int(cost), tmp_a, tmp_b])




total, MST = kruskal(edges)
print(total)
print(MST)

'''
7 12
A B C D E F G
A B 8
A C 5
B C 10
B D 2
B E 18
C D 3
C F 16
D E 12
D F 30
D G 14
E G 4
F G 26
'''
'''
'''
# 8th coding test
# 2022.11. 1.(Tue)
# Q.1
'''
'''
'''
import sys
sys.setrecursionlimit(10**6)

def find_parent(a):
    if parent[a] == a:
        return a
    p = find_parent(parent[a])
    parent[a] = p
    return parent[a]

def union_set(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return
    elif rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] == rank[b]:
        parent[a] = b
        rank[b] += 1

def kruskal(edges):
    edges.sort()
    result = 0
    MST = []
    for edge in edges:
        if edge == []:
            continue
        cost, a, b = edge
        if find_parent(a) != find_parent(b):
            union_set(a,b)
            result += cost
            MST.append((a,b))
    return result, MST

N, M = map(int, input().split())
NODE_LIST = list(map(str, input().split()))
parent = [0] * (N+1)
rank = [0] * (N+1)
parent = [i for i in range(N+1)]
edges = [[] for i in range(M+1)]

for i in range(1, M + 1):
    a, b, c = map(str, input().split())
    tmp_a = 0
    tmp_b = 0
    for j in range(0,len(NODE_LIST)):
        if NODE_LIST[j] == a:
            tmp_a = j
    for j in range(0,len(NODE_LIST)):
        if NODE_LIST[j] == b:
            tmp_b = j
    edges[i].extend([(int(c)), tmp_a+1, tmp_b+1])

total, MST = kruskal(edges)
print(total)


'''
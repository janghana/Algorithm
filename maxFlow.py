import sys
from collections import deque

totalFlow = 0
MAX_V = 100
INF = sys.maxsize

N = 6
MAX = 52
capacity = [[0] * MAX_V for _ in range(MAX)]
flow = [[0] * MAX_V for _ in range(MAX)]
flowdict = {}

def fromCtoI(target_node):
    if target_node.isdigit():
        return int(target_node)
    else:
        if target_node.isupper():
            return ord(target_node) - ord('A')
        else:
            return ord(target_node) - ord('a') + 26



start_node = fromCtoI("A")
# start one
end_node = fromCtoI("Z")
# end one

input_num = int(sys.stdin.readline())
for _ in range(input_num):
    S, T, c = sys.stdin.readline().rstrip().split()
    S = fromCtoI(S)
    T = fromCtoI(T)
    c = int(c)
    capacity[S][T] = c
    # capacity[dv][sv] = int(c)
    # flowList[S].append(T)
    # flowList[T].append(S)
    if S not in flowdict:
        flowdict[S] = [T]
    else:
        flowdict[S].append(T)
    if T not in flowdict:
        flowdict[T] = [S]
    else:
        flowdict[T].append(S)

def BFS(start_node, end_node, visit):
    dq = deque()
    dq.append(start_node)

    while dq and visit[end_node] == -1:
        S = dq.popleft()

        for T in flowdict[S]:
            if capacity[S][T] - flow[S][T] > 0 and visit[T] == -1:
                dq.append(T)
                visit[T] = S
                if T == end_node:
                    break
    if visit[end_node] == -1:
        return True
    else:
        return False
def edmonds_Karp(start_node, end_node):
    while 1:
        visit = [-1 for i in range(MAX_V)]
        if BFS(start_node, end_node, visit):
            break

        minFlow = INF

        i = end_node
        while i != start_node:
            minFlow = min(minFlow, capacity[visit[i]][i] - flow[visit[i]][i])
            i = visit[i]

        i = end_node
        while i != start_node:
            flow[visit[i]][i] += minFlow
            flow[i][visit[i]] -= minFlow
            i = visit[i]

        global totalFlow
        totalFlow += minFlow

    return totalFlow

print(edmonds_Karp(start_node, end_node))

# arr = [[1, 2, 12], [1, 4, 11], [2, 3, 6], [2, 4, 3], [2, 5, 5],
#        [2, 6, 9], [3, 6, 8], [4, 5, 9], [5, 3, 3], [5, 6, 4]]
'''
10
1 2 12
1 4 11
2 3 6
2 4 3
2 5 5
2 6 9
3 6 8
4 5 9
5 3 3
5 6 4
'''
'''
5
A B 3
B C 3
C D 5
D Z 4
B Z 6
'''

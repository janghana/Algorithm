import sys
from collections import deque

N, M = map(int,sys.stdin.readline().rstrip().split())
height_students = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    height_students[A].append(B)
    in_degree[B] += 1

def topologicalSorting(height_students):
    data_queue = deque()
    result = []

    for i in range(1, N+1):
        if in_degree[i] == 0:
            data_queue.append(i)

    while data_queue:
        current_val = data_queue.popleft()
        result.append(current_val)

        for i in height_students[current_val]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                data_queue.append(i)
    for i in result:
        print(i, end=" ")
        
topologicalSorting(height_students)


'''
3 2
1 3
2 3
'''
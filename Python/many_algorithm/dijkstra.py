import sys
import heapq

N, M = map(int, input().split())
start, end = map(str, input().split())
node_list = list(map(str, input().split()))

dp = {}
graph = {}
prev = {}
heap = []

for i in node_list:
    graph[i] = []
    dp[i] = sys.maxsize

for i in range(M):
    a, b, cost = map(str, input().split())

    graph[a].append([int(cost), b])
    graph[b].append([int(cost), a])


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        wei, now = heapq.heappop(heap)
        if dp[now] < wei:
            continue

        for w, next_n in graph[now]:
            next_w = w + wei
            if dp[next_n] > next_w:
                dp[next_n] = next_w
                prev[next_n] = now
                heapq.heappush(heap, [next_w, next_n])


dijkstra(start)

visit = []
cur = end

while cur in prev and cur != start:
    visit.append(cur)
    cur = prev[cur]
visit.append(cur)

print(''.join(reversed(visit)))
print(dp[end])

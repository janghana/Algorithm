import sys
import heapq

N, M = map(int, input().split())
final = int(input())
node_list = list(map(str, input().split()))

dp= {}
graph = {}
heap = []
result_dict = {}
for i in node_list:
    graph[i] = []
    result_dict[i] = 0

for i in range(M):
    a,b,cost = map(str, input().split())

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
                heapq.heappush(heap, [next_w, next_n])

for i in node_list:
    for k in node_list:
        dp[k] = sys.maxsize
    dijkstra(i)
    heap = []
    result_val = 0
    for j in node_list:
        if i == j:
            continue
        if final >= dp[j] :
            result_val += 1
    result_dict[i] = result_val        

        

result_val_cost = [0, '']
for i in result_dict:
    if result_dict[i] > result_val_cost[0]:
        result_val_cost[0] = result_dict[i]
        result_val_cost[1] = i
        
print(result_val_cost[1],1+result_val_cost[0])
    

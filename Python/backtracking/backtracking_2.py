from itertools import combinations
N, M = map(int ,input().split())
tmp = [i for i in range(1, N+1)]
result = list(combinations(tmp,M))
for i in result:
    print(*i)

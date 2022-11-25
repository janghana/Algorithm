import sys

N, K = map(int, sys.stdin.readline().split())
d = [[0]*(K+1) for _ in range(N+1)]

weight_bag = [[0,0]]
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    weight_bag.append([W,V])
# print(weight_bag)
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = weight_bag[i][0]
        value = weight_bag[i][1]
        if j < weight:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-weight]+value)
    # print(d)

print(d[N][K])
'''
4 7
6 13
4 8
3 6
5 12
'''
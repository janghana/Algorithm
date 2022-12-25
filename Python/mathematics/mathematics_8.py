T = int(input())

for i in range(T):
    K = int(input())
    N = int(input())
    tmp_0_li = [i for i in range(1, N+1)]
    tmp_li = [[] for _ in range(K+1)]
    tmp_val = []
    tmp_li[0].extend(tmp_0_li)
    for j in range(1,K+1):
        for k in range(1, N+1):
            tmp_li[j].append(sum(tmp_0_li[:k]))
        for p in range(len(tmp_0_li)):
            tmp_val.append(tmp_0_li[p])
        for k in range(1, N + 1):
            tmp_0_li[k-1] = sum(tmp_val[:k])
        tmp_val.clear()
    print(tmp_li[K][N-1])

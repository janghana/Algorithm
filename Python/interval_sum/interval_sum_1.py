N, M = map(int, input().split())
N_list = list(map(int, input().split()))
tmp = 0
tmp_val = []
for i in N_list:
    tmp += i
    tmp_val.append(tmp)
for i in range(M):
    i, j = map(int,input().split())
    if i == 1:
        print(tmp_val[j-1])
    else:
        print(tmp_val[j-1] - tmp_val[i-2])

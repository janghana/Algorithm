N, M = map(int, input().split())
N_list = list(map(int, input().split()))
tmp = 0
tmp_val = [sum(N_list[:M])]
for i in range(1,N - M + 1):
    tmp_val.append(tmp_val[i-1] - N_list[i-1] + N_list[i + M - 1])
print(max(tmp_val))

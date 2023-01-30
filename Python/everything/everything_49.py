N = int(input())
N_list = []
tmp = []
div = []
for i in range(N):
    N_list.append(int(input()))
    if i > 0:
        tmp.append(N_list[i] - N_list[i-1])
        div.append(N_list[i] // N_list[i-1])
if len(list(set(tmp))) == 1:
    print(N_list[N-1] + tmp[0])
else:
    print(N_list[N-1] * div[0])

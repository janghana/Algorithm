N = int(input())
N_list = list(map(int, input().split()))
tmp = 0
tmp_li = []
for i in range(1,N):
    tmp_li.append(N_list[i] - N_list[i-1])
result = 0
res_li = []
for i in tmp_li:
    if i <= 0:
        res_li.append(result)
        result = 0
    else:
        result += i
res_li.append(result)
print(max(res_li))

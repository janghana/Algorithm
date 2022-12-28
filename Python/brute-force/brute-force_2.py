N = int(input())
N_list = [i for i in range(1, N)]
result_list = []
for i in N_list:
    tmp_val = i
    for j in str(i):
        tmp_val += int(j)
    if tmp_val == N:
        result_list.append(i)
if len(result_list) == 0:
    print(0)
else:
    print(result_list[0])

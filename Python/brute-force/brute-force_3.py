N = int(input())
tmp_list = []
result_list = []
for i in range(N):
    kg, cm = map(int, input().split())
    tmp_list.append([kg, cm])
for i in tmp_list:
    cnt = 0
    for j in tmp_list:
        if i == j:
            continue
        if j[0] > i[0] and j[1] > i[1]:
            cnt += 1
    result_list.append(cnt+1)
print(*result_list)

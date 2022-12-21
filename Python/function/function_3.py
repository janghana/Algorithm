N = int(input())

cnt = 0
for i in range(N+1):
    if len(str(i)) == 1 and i > 0:
        cnt += 1
    if len(str(i)) == 2:
        cnt += 1
    else:
        tmp_val = 0
        tmp_li = []
        for j in range(len(list(str(i)))-1):
            tmp_li.append(int(list(str(i))[j+1]) - int(list(str(i))[j]))
        tmp_li = set(tmp_li)
        if len(tmp_li) == 1:
            cnt+=1
print(cnt)

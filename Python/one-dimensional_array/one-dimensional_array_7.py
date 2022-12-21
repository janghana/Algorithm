N = int(input())
OX_li = []
for i in range(N):
    OX_li.append(input())

result_li = []
for i in OX_li:
    cnt = 0
    result_val = 0
    for j in i:
        if j == "O":
            cnt += 1
        elif j == "X":
            cnt = 0
        result_val += cnt
    result_li.append(result_val)
for i in result_li:
    print(i)

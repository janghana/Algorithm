input()
num_list = list(map(int ,input().split()))

cnt = 0
for i in num_list:
    if i == 1:
        continue
    if i == 2 or i == 3:
        cnt += 1
        continue
    nTrue = True
    for j in range(2,i):
        if i % j == 0:
            nTrue = False
    if nTrue:
        cnt += 1
print(cnt)

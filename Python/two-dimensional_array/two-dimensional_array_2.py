max = -100000
cnt = 0
info = [0, 0]
for i in range(9):
    list_9 = list(map(int, input().split()))
    cnt += 1
    count = 1
    for j in list_9:
        if max < j:
            max = j
            info[0] = cnt
            info[1] = count
        count += 1

print(max)
print(info[0], info[1])

N_li = list(map(int, input().split()))

while True:
    check = True
    for i in range(1,5):
        if N_li[i-1] > N_li[i]:
            tmp = N_li[i]
            N_li[i] = N_li[i-1]
            N_li[i-1] = tmp
            check = False
            print(*N_li)
    if check:
        break

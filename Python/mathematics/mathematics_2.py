N = int(input())

cnt = 1
if N == 1:
    print(cnt)
else:
    tmp_val = 1
    while True:
        tmp_val += 6 * cnt
        if tmp_val >= N:
            print(cnt+1)
            break
        cnt += 1

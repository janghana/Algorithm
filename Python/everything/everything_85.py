T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(1,N):
        if i ** 2 <= N:
            cnt += 1
        if i ** 2 > N:
            break
    print(cnt)

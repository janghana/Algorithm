import sys
T = int(input())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    cnt = 0
    for a in range(1,N-1):
        for b in range(a+1, N):
            if ((a**2 + b**2 + M)%(a*b)) == 0:
                cnt += 1
    print(cnt)

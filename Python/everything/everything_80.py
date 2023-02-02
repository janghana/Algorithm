T = int(input())

for _ in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    N_list.sort()
    src = 0
    for i in range(1,N):
        src += N_list[i] - N_list[i-1]
    print(src * 2)

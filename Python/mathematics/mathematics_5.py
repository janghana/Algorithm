import math
T = int(input())
for i in range(T):
    H, W, N = map(int ,input().split())

    H_div_N = N % H
    H_quo_N = N // H

    if H_div_N == 0:
        H_div_N = H
        H_quo_N = math.ceil(N / H) - 1

    if H_quo_N + 1 >= 10:
        print(str(H_div_N)+str(H_quo_N +1))
    else:
        print(str(H_div_N)+"0"+str(H_quo_N +1))

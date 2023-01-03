from collections import Counter
T = int(input())

for _ in range(T):
    N = int(input())
    N_dict = {}
    for i in range(N):
        cloth, kinds = map(str,input().split())
        if kinds not in N_dict:
            N_dict[kinds] = [cloth]
        else:
            N_dict[kinds].append(cloth)
    result = 1
    for i in N_dict:
        result *= len(N_dict[i]) + 1
    print(result - 1)

N = int(input())
N_list = set(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))
result = []
for i in M_list:
    if i not in N_list:
        result.append(0)
    else:
        result.append(1)
print(*result)

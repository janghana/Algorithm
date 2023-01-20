from itertools import permutations
N = int(input())
N_list = list(map(int ,input().split()))
result = 0
for i in permutations(N_list):
    total = 0
    for j in range(1,N):
        total += abs(i[j-1] - i[j])
    if total > result:
        result = total
print(result)

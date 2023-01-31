from itertools import permutations
nanj = []
res = []
for _ in range(9):
    nanj.append(int(input()))
N = permutations(nanj,7)
for i in N:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break

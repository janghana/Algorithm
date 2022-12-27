from collections import Counter
N = input()
result = ""
C_N = Counter(sorted(N))
for i in C_N:
    for j in range(C_N[i]):
        result += i
print(sorted(N)[::-1])

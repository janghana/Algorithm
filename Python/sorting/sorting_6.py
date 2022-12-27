from collections import Counter
import sys
N = int(input())
src = []
for _ in range(N):
    src.append(int(sys.stdin.readline()))

middle_val_index = N // 2
src.sort()

C_src = Counter(src).most_common(2)
num = 0
if N == 1:
    num = src[0]
else:
    if C_src[0][1] == C_src[1][1]:
        num = C_src[1][0]
    else:
        num = C_src[0][0]
print(round(sum(src)/N))
print(src[middle_val_index])
print(num)
print(src[N-1] - src[0])

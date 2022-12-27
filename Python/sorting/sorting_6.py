import sys
N = int(input())
src = [0] * 10001

for _ in range(N):
    src[int(sys.stdin.readline())] += 1
for i in range(len(src)):
    if src[i] != 0:
        for j in range(src[i]):
            print(i)

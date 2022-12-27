import sys
N = int(input())
src = []
src_fit = [[]for i in range(50)]
for i in range(N):
    src.append(sys.stdin.readline().rstrip())
src.sort()

for i in src:
    if i in src_fit[len(i)-1]:
        continue
    src_fit[len(i)-1].append(i)
for i in src_fit:
    for j in i:
        print(j)
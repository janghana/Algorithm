import sys
N = int(input())

src = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    src.append([y, x])

for x, y in sorted(src):
    print(y, x)

'''
5
3 4
1 1
1 -1
2 2
3 3
'''
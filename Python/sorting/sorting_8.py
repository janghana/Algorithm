N = int(input())

src = []
for i in range(N):
    src.append(list(map(int, input().split())))

for x, y in sorted(src):
    print(x, y)

'''
5
3 4
1 1
1 -1
2 2
3 3
'''
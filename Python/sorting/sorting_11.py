N = int(input())
src = []
src_two = [[] for i in range(200)]
for i in range(N):
    src.append(list(map(str,input().split())))
for i in src:
    src_two[int(i[0]) - 1].append([i[0],i[1]])
for i in src_two:
    for j in i:
        print(j[0], j[1])

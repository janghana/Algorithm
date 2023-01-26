li = []
for _ in range(7):
    N = int(input())
    if N % 2 != 0:
        li.append(N)

if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(min(li))

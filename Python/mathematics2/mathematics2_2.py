A = int(input())
B = int(input())
num_list = [i for i in range(A, B+1)]

result = []
for i in num_list:
    if i == 1:
        continue
    if i == 2:
        result.append(2)
        continue
    if i == 3:
        result.append(3)
        continue
    nTrue = True
    for j in range(2,i):
        if i % j == 0:
            nTrue = False
    if nTrue:
        result.append(i)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    result.sort()
    print(result[0])

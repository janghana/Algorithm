A, B = map(int, input().split())
result = []
for i in range(1,A+1):
    if A % i == 0:
        result.append(i)
if len(result) < B:
    print(0)
else:
    print(result[B - 1])

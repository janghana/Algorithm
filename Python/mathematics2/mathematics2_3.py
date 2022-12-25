N = int(input())

result = []
nTrue = True
if N == 1:
    nTrue = False
for j in range(2, N):
    if N % j == 0:
        nTrue = False
if nTrue:
    print(N)
else:
    for i in range(2,N+1):
        if N % i == 0:
            while N % i == 0:
                N = N // i
                result.append(i)
for i in result:
    print(i)
N = int(input())
for i in range(N):
    b, a = map(int ,input().split())
    result = 1
    for i in range(a,a-b,-1):
        result *= i
    for i in range(b,1,-1):
        result //= i
    print(result)
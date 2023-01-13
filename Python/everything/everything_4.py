def fibonacci(a,b, N):
    for _ in range(N):
        a,b = a + b , a
    return a
N = int(input())
a,b = 0, 1
print(fibonacci(a,b,N))
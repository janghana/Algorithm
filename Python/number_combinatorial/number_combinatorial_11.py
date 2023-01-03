N = int(input())

def factorial(N):
    if N == 1:
        return 1
    if N == 0:
        return 1
    return N * factorial(N - 1)

cnt = 0
for i in reversed(str(factorial(N))):
    if i != '0':
        break
    cnt += 1
print(cnt)

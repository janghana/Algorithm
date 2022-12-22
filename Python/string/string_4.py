N = int(input())

for _ in range(N):
    num, ch = map(str, input().split())
    result = ''
    for i in ch:
        result += i*int(num)
    print(result)

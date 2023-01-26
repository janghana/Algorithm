T = int(input())

for _ in range(T):
    max_ = -10000
    result = ""
    for i in range(int(input())):
        S, num = map(str, input().split())
        if int(num) > max_:
            max_ = int(num)
            result = S
    print(result)

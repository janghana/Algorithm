N = int(input())
a,b = map(int, input().split())

max_ = a // 2 + b

if max_ > N:
    print(N)
elif max_ < N:
    print(max_)

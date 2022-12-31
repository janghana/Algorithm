A = int(input())
A_list = list(map(int, input().split()))

if A == 1:
    print(A_list[0] ** 2)
else:
    print(min(A_list) * max(A_list))



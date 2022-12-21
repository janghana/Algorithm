input()
num_list = list(map(int, input().split()))
min_ = 10000000
max_ = -10000000
for i in num_list:
    if min_ > i:
        min_ = i
    if max_ < i:
        max_ = i

print(min_, max_)
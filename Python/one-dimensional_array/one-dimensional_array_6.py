N = int(input())
num_li = list(map(int ,input().split()))

max_ = -1000000
result_li = []
for i in num_li:
    if max_ < i:
        max_ = i
for i in num_li:
    result_li.append(i / max_ * 100)
result_val = 0
for i in result_li:
    result_val += i
print(result_val/N)
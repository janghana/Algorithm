max_ = 0
victory = 0
for i in range(5):
    li = list(map(int, input().split()))
    if max_ < sum(li):
        max_ = sum(li)
        victory = i + 1
print(victory, max_)

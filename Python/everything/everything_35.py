cost, t, total = map(int ,input().split())
if cost * t - total >= 0:
    print(cost * t - total)
else:
    print(0)

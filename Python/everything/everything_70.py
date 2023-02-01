xyz = list(map(int, input().split()))
order = input()
res = []
max_ = max(xyz)
min_ = min(xyz)
xyz.remove(max(xyz))
xyz.remove(min(xyz))
for i in order:
    if i == "C":
        res.append(max_)
    elif i == "A":
        res.append(min_)
    elif i == "B":
        res.append(xyz[0])
print(*res)

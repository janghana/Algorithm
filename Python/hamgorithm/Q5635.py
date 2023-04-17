li = []
for _ in range(int(input())):
    name, d,m,y = list(map(str, input().split()))
    if len(m) == 1:
        m = '0'+m
    if len(d) == 1:
        d = '0' + d
    tmp = y+m+d

    li.append([name, int(tmp)])
max_ = 0
min_ = 100000000
max_result = ''
min_result = ''
for i in li:
    if max_ < i[1]:
        max_ = i[1]
        max_result = i[0]
    if min_ > i[1]:
        min_ = i[1]
        min_result = i[0]
print(max_result)
print(min_result)

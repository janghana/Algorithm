from collections import Counter
li = []
while True:
    try:
        tmp = input().split()
        for i in tmp:
            for j in i:
                li.append(j)
    except:
        break
max_ = max(Counter(li).values())
result = []
for i in Counter(li):
    if max_ == Counter(li)[i]:
        result.append(i)
for i in sorted(result):
    print(i, end="")

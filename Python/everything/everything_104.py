re = []
max_ = 0
result = ""
for i in range(5):
    re.append(input())
    if max_ < len(re[i]):
        max_ = len(re[i])
for i in range(1,max_+1):
    for j in re:
        result += j[i-1:i]
print(result)

from collections import Counter
N = int(input())
tmp = []
for _ in range(N):
    li = Counter(list(map(int, input().split())))
    result = 0
    if len(li) == 1:
        for i in li:
            result += 50000 + i * 5000
    elif len(li) == 2:
        for i in li:
            if li[i] == 3:
                result += 10000 + i * 1000
                result -= 2000
            elif li[i] == 2:
                result += i * 500
        result += 2000
    elif len(li) == 3:
        for i in li:
            if li[i] == 2:
                result += 1000 + i * 100
    elif len(li) == 4:
        max_ = -1000000
        for i in li:
            if max_ < i:
                max_ = i
        result += max_ * 100
    tmp.append(result)
print(max(tmp))

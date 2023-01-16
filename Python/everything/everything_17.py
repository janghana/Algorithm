from collections import Counter
T = int(input())
result = []
for _ in range(T):
    abc_list = list(map(int, input().split()))
    abc = Counter(abc_list)
    for i in abc:
        if len(abc) == 1:
            result.append(10000 + i * 1000)
            break
        elif abc[i] == 2:
            result.append(1000 + i * 100)
            break
        elif len(abc) == 3:
            result.append(max(abc) * 100)
            break
print(max(result))

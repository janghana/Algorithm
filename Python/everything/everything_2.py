from collections import Counter
N = int(input())
result = []
for _ in range(N):
    result.append(int(input()))
if Counter(result)[0] > Counter(result)[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
import math
N = int(input())

tmp_list = []
for i in range(N):
    tmp_list.append(int(input()))
tmp_list.sort()
interval_list = []
result_list = []

for i in range(1, N):
    interval_list.append(tmp_list[i] - tmp_list[i-1])

prev = interval_list[0]
for i in range(1, len(interval_list)):
    prev = math.gcd(prev, interval_list[i])

for i in range(2, int(math.sqrt(prev)) + 1):
    if prev % i == 0:
        result_list.append(i)
        result_list.append(prev//i)

result_list.append(prev)
result_list = list(set(result_list))
result_list.sort()
print(*result_list)

from itertools import combinations

N, M = map(int, input().split())
blackjak_list = list(map(int, input().split()))
sum_list = []
check_equal = False
result = M
for i in list(combinations(blackjak_list, 3)):
    tmp_val = sum(list(i))
    if tmp_val == M:
        check_equal = True
        break
    elif tmp_val < M:
        sum_list.append(M - tmp_val)
if check_equal:
    print(result)
else:
    sum_list.sort()
    result -= sum_list[0]
    print(result)

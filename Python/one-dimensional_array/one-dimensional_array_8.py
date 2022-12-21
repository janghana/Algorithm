N = int(input())

for _ in range(N):
    num_list = list(map(int, input().split()))
    rate = num_list[0]
    result_val = 0
    for i in range(1,len(num_list)):
        result_val += num_list[i]
    result_tmp = result_val/rate
    cnt = 0
    for i in num_list[1:]:
        if result_tmp < i:
            cnt += 1
    print("{:.3f}".format(cnt/rate * 100)+"%")

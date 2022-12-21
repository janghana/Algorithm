N, X = map(int, input().split())
num_list = list(map(str, input().split()))
result_list = []
count = 0
for i in num_list:
    if int(i) < X:
        result_list.append(i)

print(' '.join(result_list))

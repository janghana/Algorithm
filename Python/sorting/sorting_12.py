N = int(input())
num_list = list(map(int ,input().split()))
num_val = sorted(list(set(num_list)))
num_dict = {}
for i in range(len(num_val)):
    num_dict[num_val[i]] = i
for i in num_list:
    print(num_dict[i], end=" ")

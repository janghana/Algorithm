import sys

input()
p_list = list(map(int,input().split()))
input()
l_list = list(map(int,input().split()))

result_list = []

for i in p_list:
    max_val = 10000
    for j in l_list:
        if max_val > abs(i-j):
            max_val = abs(i-j)
    result_list.append(max_val)

result_list.sort()
print(result_list[-1])

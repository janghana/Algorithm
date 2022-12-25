N = int(input())

num_5 = N // 5
num_3 = N // 3

cnt_max = -1

for i in range(num_5+1):
    for j in range(num_3+1):
        if i*5 + j*3 == N:
            cnt_max = i + j

print(cnt_max)
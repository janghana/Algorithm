N_list = list(map(int ,input().split()))
result = 0
for i in N_list:
    result += i**2
print(result % 10)

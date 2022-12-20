import  sys
num = int(input())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0 for i in range(num)]

for i in range(num):
    for j in range(i):
        if num_list[i] > num_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    # print(dp)
print(max(dp))
'''
6
10 20 10 30 20 50
'''

# n = int(input())
# a = list(map(int, input().split()))
# dp = [0 for i in range(n)]
# for i in range(n):
#     for j in range(i):
#         if a[i] > a[j] and dp[i] < dp[j]:
#             dp[i] = dp[j]
#     dp[i] += 1
# print(max(dp))
import sys
input = sys.stdin.readline

dp = [1,2,4,7]
T = int(input())
for i in range(T):
    num = int(input())
    for j in range(len(dp), num):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
        # print(dp)
    print(dp[num-1])
'''
3
4
7
10
'''
import  sys
num = int(input())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

privious_sum = [num_list[0]]
# print(*num_list)
# print(privious_sum)
cnt = 0
for i in range(1, num+1):
    print(privious_sum)
    if i > 1:
        print(privious_sum[-1], privious_sum[-2])
        if privious_sum[-1] > privious_sum[-2]:
            cnt += 1
    if i == num:
        break
    privious_sum.append(max(num_list[i], privious_sum[i-1] + num_list[i]))

# print(*privious_sum)
print(max(privious_sum[:]))
print(cnt)

# # 1912: 400 - 다이나믹 프로그래밍 1 - 연속합
# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0] * n # arr[i]까지 고려했을 때 최대 연속합
# dp[0] = arr[0]
# for i in range(1, n):
#     dp[i] = max(arr[i], dp[i-1]+arr[i]) # arr[i] 혹은 이전 최대 연속합+arr[i]
# print(max(dp))

'''
10
10 -4 3 1 5 6 -35 12 21 -1

O(n^2)의 복잡도
'''
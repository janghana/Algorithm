import sys

INIT_MIN = -sys.maxsize - 1

def cutRod_DP(price, n):
    val = [0 for x in range(n + 1)]
    val[0] = 0
    for i in range(1, n + 1):
        # print(val)
        max_val = INIT_MIN
        for j in range(1, i//2):
            max_val = max(price[j-1] + price[n-j-1], max_val)
        val[n] = max_val
    return val[n]

def main():
    n = int(input())
    input_list = list(map(int, input().split()))
    print(cutRod_DP(input_list, len(input_list)))


if __name__:
    main()


'''
8
1 5 8 9 10 17 17 20
'''
def lis(input_int):
    n = len(input_int)
    length = [1] * n

    for i in range(1, n):
        for j in range(i):
            if input_int[j] < input_int[i]:
                length[i] = max(length[i], length[j] + 1)
                #print("i: ", i, " j: ", j, "length[i]: ", length[i])
    #print(length)
    return(max(length))

def main():
    test_case = int(input())
    for _ in range(test_case):
        input_int = list(map(int, input().split()))
        print(lis(input_int))

if __name__ == '__main__':
    main()

'''
2
3 5 7 9 2 1 4 8
1 7 3 4 2 8 5 6 9 10
'''
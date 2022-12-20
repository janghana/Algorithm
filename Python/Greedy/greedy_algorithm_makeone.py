def main():
    n, k = map(int, input().split())

    result = 0

    while True:
        target = (n/k)*k
        result += (n - target)
        n = target
        if n < k :
            break
        n //= k

        result += 1

        print(n, target, result)

    result += ( n - 1 )
    print(result)

if __name__=="__main__":
    main()

'''
25 3
'''
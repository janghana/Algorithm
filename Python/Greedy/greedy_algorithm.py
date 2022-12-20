def main():
    n = int(input())
    coin = list(map(int, input().split()))

    count = 0

    for c in coin:
        count += n // c
        n %= c

    print(count)


if __name__ == "__main__":
    main()
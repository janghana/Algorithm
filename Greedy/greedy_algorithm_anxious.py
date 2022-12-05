def main():
    n = int(input())
    group = list(map(int, input().split()))
    group.sort()

    result = 0
    count = 0

    for x in group:
        count += 1
        if count >= x:
            count = 0
            result += 1

    print(result)


if __name__ == "__main__":
    main()
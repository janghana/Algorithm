N = int(input())

for i in range(N):
    N_list = list(map(str, input().split()))
    num = float(N_list[0])
    for j in N_list[1:]:
        if j == "@":
            num *= 3
        elif j == "%":
            num += 5
        elif j == "#":
            num -= 7
    print(f'{num:.2f}')

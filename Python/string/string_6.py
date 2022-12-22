N1, N2 = map(str, input().split())
if int(N1[::-1]) > int(N2[::-1]):
    print(N1[::-1])
else:
    print(N2[::-1])
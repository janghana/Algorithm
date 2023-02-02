e, f, c = map(int, input().split())
S = e + f
i = 0
while S >= c:
    i += S // c
    S = S // c + S % c
print(i)
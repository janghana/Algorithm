result = []
while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a > b > c or a > c > b:
        length_max = pow(a, 2)
        length_1 = pow(b,2)
        length_2 = pow(c,2)
    elif b > a > c or b > c > a:
        length_max = pow(b, 2)
        length_1 = pow(a,2)
        length_2 = pow(c,2)
    elif c > a > b or c > b > a:
        length_max = pow(c, 2)
        length_1 = pow(a,2)
        length_2 = pow(b,2)
    if length_max == length_1 + length_2:
        result.append("right")
    else:
        result.append("wrong")
for i in result:
    print(i)

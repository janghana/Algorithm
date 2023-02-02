res = int(input())
while True:
    S = input()
    if S == "=":
        break
    N = int(input())
    if S == "+":
        res += N
    elif S == "-":
        res -= N
    elif S == "*":
        res *= N
    elif S == "/":
        res //= N
print(res)

'''
10
-
21
*
5
=
'''
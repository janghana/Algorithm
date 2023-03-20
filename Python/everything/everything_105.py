import math

A, B = map(int, input().split())
C, D = map(int, input().split())
X = A * D + C * B
Y = B * D
print(X // math.gcd(X, Y), Y // math.gcd(X, Y))


# Z = A+C
# X = A*D + C*B
# if B == D:
#     while math.gcd(Z, B) != 1:
#         Z = Z // math.gcd(Z, B)
#         B = B // math.gcd(Z, B)
#     print(A+C, B)
#
# else:
#     Y = math.lcm(B,D)
#     while math.gcd(X, Y) != 1:
#         X = X // math.gcd(X, Y)
#         Y = Y // math.gcd(X, Y)
#     print(X, Y)

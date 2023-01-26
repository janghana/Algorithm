N = int(input())

A = 300
B = 60
C = 10
div_A = 0
div_B = 0
div_C = 0

div_A = N // A
N -= div_A * A
div_B = N // B
N -= div_B * B
div_C = N // C

if N % 10 != 0:
    print(-1)
elif div_A * A + div_B * B + div_C * C:
    print(div_A, div_B, div_C)

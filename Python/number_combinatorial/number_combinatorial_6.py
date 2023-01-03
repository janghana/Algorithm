from fractions import Fraction
import math
N = int(input())
N_list = list(map(int, input().split()))

for i in N_list[1:]:
    num = Fraction(N_list[0] // math.gcd(i, N_list[0]), i // math.gcd(i, N_list[0]))
    print(str(num.numerator)+'/'+str(num.denominator))

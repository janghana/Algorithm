def GCD_DP(a,b):
    if b == 0:
        return a
    return GCD_DP(b, a%b)
def LCM(a,b):
    return (a*b) // GCD_DP(a,b)

N = int(input())

for i in range(N):
    a, b = map(int ,input().split())
    print(LCM(a,b))
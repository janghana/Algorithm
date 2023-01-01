a, b = map(int ,input().split())

def GCD(a,b):
    while b:
        a,b = b, a%b
    return a
def GCD_DP(a,b):
    if b == 0:
        return a
    return GCD_DP(b, a%b)

def LCM(a,b):
    return (a*b) // GCD_DP(a,b)

print(GCD_DP(a,b))
print(LCM(a,b))
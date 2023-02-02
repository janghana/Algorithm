T = int(input())
while True:
    N = int(input())
    if N == 0:
        break
    if N % T == 0:
        print(N,"is a multiple of",str(T)+".")
    elif N % T != 0:
        print(N,"is NOT a multiple of",str(T)+".")

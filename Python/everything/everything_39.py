S = input()
nTrue = 1
for i in range(0,len(S)//2):
    if S[i] != S[len(S) - i - 1]:
        nTrue = 0
print(nTrue)

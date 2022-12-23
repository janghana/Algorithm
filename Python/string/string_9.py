N = int(input())
cnt = 0

for i in range(N):
    S = input()
    nTrue = True
    S_dict = {}
    for j in S:
        S_dict[j] = []
    for j in S_dict:
        for k in range(len(S)):
            if j == S[k]:
                S_dict[j].append(k)
    for j in S_dict:
        if len(S_dict[j]) == 1:
            continue
        for k in range(len(S_dict[j])-1):
            if abs(S_dict[j][k+1] - S_dict[j][k]) != 1:
                nTrue = False
    if nTrue == True:
        cnt += 1
print(cnt)

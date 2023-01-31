while True:
    S = input()
    nTrue = True
    if S == '0':
        break
    for i in range(0, len(S)//2):
        if S[i] != S[len(S) - i - 1]:
            nTrue = False
    if nTrue:
        print('yes')
    else:
        print('no')

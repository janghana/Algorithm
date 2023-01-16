from collections import Counter
for _ in range(3):
    N_list = list(map(int,input().split()))
    C_list = Counter(N_list)
    for i in C_list:
        if C_list[i] == 4:
            if i == 0:
                print('D')
                break
            elif i == 1:
                print('E')
                break
        elif C_list[i] == 2:
            print('B')
            break
        elif C_list[i] == 1:
            if i == 0:
                print('A')
                break
            elif i == 1:
                print('C')
                break
        elif C_list[i] == 3:
            if i == 0:
                print('C')
                break
            elif i == 1:
                print('A')
                break

num_l = input()

char_l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cnt = 0
char_dict = {}
for i in num_l:
    if i in char_dict:
        cnt += 1
        continue
    char_dict[i] = cnt
    cnt += 1
for i in char_dict:
    for j in range(len(char_l)):
        if char_l[j] == i:
            char_l[j] = str(char_dict[i])
for i in range(len(char_l)):
    if not str(char_l[i]).isdigit():
        char_l[i] = str(-1)

print(' '.join(char_l))

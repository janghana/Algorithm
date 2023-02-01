from collections import Counter
S = input()
result = 0
for i in Counter(S):
    if i.lower() == 'a':
        result += Counter(S)[i]
    elif i.lower() == 'e':
        result += Counter(S)[i]
    elif i.lower() == 'i':
        result += Counter(S)[i]
    elif i.lower() == 'o':
        result += Counter(S)[i]
    elif i.lower() == 'u':
        result += Counter(S)[i]
print(result)

S = input()
result = set()
for i in range(len(S)):
    for subset in range(i, len(S)):
        result.add(S[i:subset+1])
print(len(result))

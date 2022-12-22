S = input()

S_dict = {}
for i in S:
    if i.upper() not in S_dict:
        S_dict[i.upper()] = [0]
    elif i.upper() in S_dict:
        S_dict[i.upper()].append(0)
result = ""
max_ = -10000
for i in S_dict:
    if len(S_dict[i]) > max_:
        max_ = len(S_dict[i])
        result = i
cnt = 0
for i in S_dict:
    if len(S_dict[i]) == max_:
        cnt += 1
if cnt > 1:
    print("?")
else:
    print(result)

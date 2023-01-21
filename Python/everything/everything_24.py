from collections import Counter
li = []
while True:
    tmp = input()
    if tmp == "#":
        break
    for i in tmp.split():
        for j in i:
            li.append(j)
    result = 0
    for i in Counter(li):
        if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
            result += Counter(li)[i]
    print(result)
    li.clear()

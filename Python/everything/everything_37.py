li = input()
prev = li[0]
result = 10
for i in li[1:]:
    if i == prev:
        result += 5
    elif i != prev:
        result += 10
    prev = i
print(result)

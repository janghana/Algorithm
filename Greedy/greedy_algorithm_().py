import sys

input = sys.stdin.readline
data = input().split('-')
ans = 0
for i in data[0].split('+'):
    ans += int(i)
    # print(ans)
for i in data[1:]:
    for j in i.split('+'):
        ans -= int(j)
print(ans)

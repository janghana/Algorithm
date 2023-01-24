S = int(input())
cnt = 1
result = 0
while cnt  * (cnt + 1) / 2  <= S:
    cnt += 1
print(cnt - 1)

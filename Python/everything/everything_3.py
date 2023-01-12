N = int(input())
M = int(input())
tmp = int(str(N)[:-2]+'00')
while True:
    if tmp % M == 0:
        break
    tmp += 1
print(str(tmp)[-2:])

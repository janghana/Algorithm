count = 0
max_ = -100000000
cnt = 0
while True:
    try:
        count+=1
        N = int(input())
        if N > max_:
            max_ = N
            cnt = count
    except:
        break
print(max_)
print(cnt)

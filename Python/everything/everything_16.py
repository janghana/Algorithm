max_ = -1
tmp = 0
while True:
    try:
        inp, outp = map(int, input().split())
        tmp += outp - inp
        if tmp > max_:
            max_ = tmp
    except:
        break
print(max_)
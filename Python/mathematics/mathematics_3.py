N = int(input())

cnt = 1
result = 1
while True:
    if N == 1:
        print("1/1")
        break
    elif N <= result:
        size = cnt + 1
        if cnt % 2 == 0:
            start, end = result - cnt + 1, result
            tmp_N = N - start
            val_list = []
            for i in range(1, size):
                val_list.append((i,size-i))
            print(str(val_list[tmp_N][0])+"/"+str(val_list[tmp_N][1]))
            break
        elif cnt % 2 == 1:
            start, end = result - cnt + 1, result
            tmp_N = N - start
            val_list = []
            for i in range(size-1, 0, -1):
                val_list.append((i,size-i))
            print(str(val_list[tmp_N][0])+"/"+str(val_list[tmp_N][1]))
            break
    cnt += 1
    result += cnt

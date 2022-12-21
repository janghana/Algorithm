result_li = [i for i in range(1,10000)]
tmp_li = []
for i in range(1,10000):
    tmp_val = 0
    for j in str(i):
        tmp_val += int(j)
    tmp_val += i
    if tmp_val < 10000:
        tmp_li.append(tmp_val)
for i in list(set(tmp_li)):
    result_li.remove(i)
for i in result_li:
    print(i)
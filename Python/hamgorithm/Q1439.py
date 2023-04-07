S = input()
def find_edges(target):
    cnt = 0
    tmp = int(target[0])
    for find_me in target:
        if int(find_me) != tmp:
            cnt += 1
        tmp = int(find_me)
    if cnt % 2 == 1:
        return cnt // 2 + 1
    else:
        return cnt//2

print(find_edges(S))

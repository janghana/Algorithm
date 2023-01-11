N = int(input())

result = 0
r = [0] * N

def is_OK(num):
    for i in range(num):
        if r[num] == r[i] or abs(r[num] - r[i]) == abs(num - i):
            return False
    return True

def N_QUEEN(num):
    global result
    if num == N:
        result += 1
        return
    else:
        for i in range(N):
            r[num] = i
            if is_OK(num):
                N_QUEEN(num + 1)
N_QUEEN(0)
print(result)

N, M = map(int, input().split())

def cnt(N, divide):
    count = 0
    while N:
        N //= divide
        count += N
    return count

N_5_cnt = cnt(N,5)
M_5_cnt = cnt(M,5)
NM_5_cnt = cnt(N-M,5)

N_2_cnt = cnt(N,2)
M_2_cnt = cnt(M,2)
NM_2_cnt = cnt(N-M,2)

cnt_5 = N_5_cnt - M_5_cnt - NM_5_cnt
cnt_2 = N_2_cnt - M_2_cnt - NM_2_cnt

print(min(cnt_2, cnt_5))

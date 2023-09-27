'''
Method : Typing Studying

title : position

condition

N, score, P

which position chulsu will have ?

'''


N, new_score, P = map(int, input().split())

if N == 0:
    print(1)
else:
    cur_score = list(map(int, input().split()))
    if N == P and cur_score[-1] >= new_score:
        print(-1)
    else:
        result = N + 1
        for i in range(N):
            if cur_score[i] <= new_score:
                result = i + 1
                break
        print(result)


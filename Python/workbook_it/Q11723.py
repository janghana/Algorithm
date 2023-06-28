'''
add -> +
remove -> -
check -> S에 x 있으면 1 없으면 0
toggle -> x 있으면 제거 없으면 추가
all -> S 1 ~ 20으로 바꿈
empty -> S를 공집합으로 바꿈
'''
import sys

S = set()
N = int(sys.stdin.readline())

for _ in range(N):
    word_and_x = sys.stdin.readline().strip().split()
    if len(word_and_x) == 1:
        if word_and_x[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif word_and_x[0] == 'empty':
            S = set()
    else:
        word, x = word_and_x[0], word_and_x[1]
        x = int(x)
        if word == 'add':
            S.add(x)
        elif word == 'remove':
            S.discard(x)
        elif word == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif word == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)

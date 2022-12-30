from collections import Counter

N, M =map(int ,input().split())
i_cant_listen = []
i_cant_see = []
for i in range(N):
    i_cant_listen.append(input())
for i in range(M):
    i_cant_see.append(input())
C_i_cant_listen = Counter(i_cant_listen)
C_i_cant_see = Counter(i_cant_see)
result = []
for i in C_i_cant_listen:
    if i in C_i_cant_see:
        result.append(i)
print(len(result))
result.sort()
for i in result:
    print(i)
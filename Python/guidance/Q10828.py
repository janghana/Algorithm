N, K = map(int, input().split())
medals = []
for _ in range(N):
    medals.append(list(map(int, input().split())))

medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

target_index = [medals[i][0] for i in range(N)].index(K)

for i in range(N):
    if medals[target_index][1:] == medals[i][1:]:
        print(i + 1)
        break

'''
1. 금메달 수가 더 많은 나라
2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

N -> 각 국가
한 국가의 등수 -> 자신보다 더 잘한 나라 수 + 1
금은동 모두 같으면 같은 등수.

'''

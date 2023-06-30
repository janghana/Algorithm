'''

N

각 row에 따라 몇 번 씩 줄 설지 생각하기.
나보다 키 큰 애 찾는데, 그 애가 어디에 있는지 생각하고 그 사이의 개수를 세면 됨.

결국 버블 소트 몇 번하냐 문제.
'''


def Bubble_Sort(li):
    cnt = 0
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                cnt += 1
    return cnt


N = int(input())

for i in range(N):
    res = list(map(int, input().split()))
    count, people = res[0], res[1:]
    print(count, Bubble_Sort(people))

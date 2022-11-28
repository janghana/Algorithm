import sys

num = int(input())

num_list = []

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else :
        return (solution(n-1) + solution(n-2) + solution(n-3)) % 1000000009

for _ in range(num):
    num_list.append(solution(int(input())))

for i in num_list:
    print(i)
'''
3
4
7
10
'''

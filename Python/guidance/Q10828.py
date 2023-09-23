'''
typing study methods

-> stack

push X -> 정수 X를 스택에 넣는 연산.
pop -> 스택에서 가자 위 정수 빼고 그 수 출력. 없으면 -1
size -> 스택에 들어있는 정수 개수 출력
empty -> 스택 비어있으면 1, 아니면 0
top -> 스택 가장 위 정수 출력. 없으면 -1

'''

import sys

input = sys.stdin.readline

stack = []
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

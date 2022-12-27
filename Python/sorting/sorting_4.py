import sys
N = int(input())
src = []

def sorting(src):
    if len(src) < 2:
        return src
    mid = len(src) // 2
    left = sorting(src[:mid])
    right = sorting(src[mid:])
    return merge(left, right)

def merge(left, right):
    new_li = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            new_li.append(right[j])
            j += 1
        else:
            new_li.append(left[i])
            i += 1
    new_li += right[j:]
    new_li += left[i:]
    return new_li

for _ in range(N):
    src.append(int(sys.stdin.readline()))
for i in sorting(src):
    print(i)

a, b = map(int ,input().split())
li = [i for i in range(0, 100000)]
print(sum(li[a:b+1]))

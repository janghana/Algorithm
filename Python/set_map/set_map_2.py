N, M = map(int ,input().split())
prev_str = set()
config_str = []
for i in range(N):
    prev_str.add(input())
for i in range(M):
    config_str.append(input())
result = 0
for i in config_str:
    if i in prev_str:
        result += 1
print(result)

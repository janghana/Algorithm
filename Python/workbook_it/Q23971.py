import math
H, W, N, M = map(int, input().split())

row = math.ceil(H / (N + 1))
col = math.ceil(W / (M + 1))
print(row * col)

# 행, 열 별로 앉을 수 있는 자리 개수를 구해 곱한다.
# 앉을 수 있는 자리 개수는 {길이 / ( 비우고 앉아야 하는 자리 개수 + 1)}을 반올림 한 값이다.

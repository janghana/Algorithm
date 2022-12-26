N, M = map(int, input().split())

matrix_A = [[] for _ in range(N)]
matrix_B = [[] for _ in range(N)]
for i in range(N):
    A_list = list(map(int ,input().split()))
    for j in range(M):
        matrix_A[i] = A_list

for i in range(N):
    B_list = list(map(int ,input().split()))
    for j in range(M):
        matrix_B[i] = B_list

matrix = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        matrix[i][j] = matrix_A[i][j] + matrix_B[i][j]

for i in matrix:
    print(*i)

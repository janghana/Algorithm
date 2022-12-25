A, B = map(int, input().split())
num_list = [i for i in range(A, B+1)]
result = []

arr = [True] * (B+1)
arr[0] = False
arr[1] = False

for i in range(2, B + 1):
    if arr[i] == True:
        j = 2
        while (i * j) <= B:
            arr[i*j] = False
            j += 1

for i in range(len(arr)):
    if arr[i] is not False:
        result.append(i)

A_arr = [True] * (A+1)
A_arr[0] = False
A_arr[1] = False

for i in range(2, A + 1):
    if A_arr[i] == True:
        j = 2
        while (i * j) <= A:
            A_arr[i * j] = False
            j += 1
for i in range(len(A_arr)-1):
    if A_arr[i] is not False:
        result.remove(i)

for i in result:
    print(i)
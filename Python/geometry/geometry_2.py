from collections import Counter
C_x = []
C_y = []
for _ in range(3):
    x,y = map(int,input().split())
    C_x.append(x)
    C_y.append(y)
C_X = Counter(C_x)
C_Y = Counter(C_y)
x = ''
y = ''
for i in C_X:
    if C_X[i] == 1:
        x = i
for i in C_Y:
    if C_Y[i] == 1:
        y = i
print(x,y)

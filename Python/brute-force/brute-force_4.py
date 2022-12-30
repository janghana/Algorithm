N ,M = map(int, input().split())
black_and_white = []
for i in range(N):
    black_and_white.append(input())

result = []
for x in range(N - 7):
    for y in range(M - 7):
        start_with_B = 0
        start_with_W = 0
        for i in range(8):
            for j in range(8):
                if (x+i + y+j) % 2 == 0:
                    if black_and_white[x+i][y+j] != "B":
                        start_with_W += 1
                    if black_and_white[x+i][y+j] != "W":
                        start_with_B += 1
                else:
                    if black_and_white[x+i][y+j] != "W":
                        start_with_W += 1
                    if black_and_white[x+i][y+j] != "B":
                        start_with_B += 1
        result.append(start_with_W)
        result.append(start_with_B)
print(min(result))

T = int(input())

result = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    circle_dictance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if circle_dictance == 0 and r1 == r2:
        result.append(-1)
    elif abs(r1 - r2) < circle_dictance and circle_dictance < r1 + r2:
        result.append(2)
    elif abs(r1 - r2) == circle_dictance or circle_dictance == r1 + r2:
        result.append(1)
    else:
        result.append(0)
for i in result:
    print(i)

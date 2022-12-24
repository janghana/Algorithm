A, B, V = map(int, input().split())

A_B_sub = A - B
cnt = (V - B) // A_B_sub
result_V = cnt * A_B_sub + B
if V != result_V:
    print(cnt + 1)
else:
    print(cnt)

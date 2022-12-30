T = int(input())

for _ in range(T):
    start_x, start_y, target_x, target_y = map(int, input().split())
    count = 0
    for j in range(int(input())):
        other_x, other_y, other_r = map(int ,input().split())
        circlr_distance_1 = ((start_x - other_x)**2 + (start_y - other_y)**2)**0.5
        circlr_distance_2 = ((target_x - other_x)**2 + (target_y - other_y)**2)**0.5

        if circlr_distance_1 < other_r and circlr_distance_2 > other_r or circlr_distance_1 > other_r and circlr_distance_2 < other_r:
            count += 1
    print(count)

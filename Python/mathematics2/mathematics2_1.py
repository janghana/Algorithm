default_cost, factory_cost, product_cost = map(int, input().split())

cnt = 0
if factory_cost >= product_cost:
    print(-1)
else:
    while True:
        cnt += 10000
        if default_cost + factory_cost * cnt < product_cost * cnt:
            break
    while True:
        cnt -= 1
        if default_cost + factory_cost * cnt >= product_cost * cnt:
            break
    print(cnt+1)

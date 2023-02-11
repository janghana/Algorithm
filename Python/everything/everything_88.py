for i in range(1,int(input())+1):
    li = sorted(map(int, input().split()))
    if li[0]**2 + li[1]**2 == li[2]**2:
        print("Scenario #",end="")
        print(i,end="")
        print(':')
        print("yes\n")
    else:
        print("Scenario #",end="")
        print(i,end="")
        print(':')
        print("no\n")

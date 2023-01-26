while True:
    N = int(input())
    if N == -1:
        break
    div = []
    for i in range(1,N):
        if N % i == 0:
            div.append(i)
    if sum(div) != N:
        print(N, "is NOT perfect.")
    else:
        print(N,end=" = ")
        for i in range(len(div)):
            if len(div) - 1 == i:
                print(div[i])
                break
            print(div[i],end=" + ")

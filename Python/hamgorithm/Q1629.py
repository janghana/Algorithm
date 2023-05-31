def Divide_and_Conquer(a, b):
    if b == 1:
        return a % C
    else:
        temp = Divide_and_Conquer(a, b // 2)
        if b % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * a % C


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = Divide_and_Conquer(A, B)
    print(result)

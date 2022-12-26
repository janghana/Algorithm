def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
for i in range(N):
    A = int(input())

    num1, num2 = A // 2, A // 2

    while num1 > 0:
        if is_prime(num1) and is_prime(num2):
            print(num1, num2)
            break
        num1 -= 1
        num2 += 1


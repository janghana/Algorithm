N = int(input())
result = 0
for i in range(1,N):
    result += i * (i - 1) // 2
print(result)
print(3)
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''
import time

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == '__main__':
    main()

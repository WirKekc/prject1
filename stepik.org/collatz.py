a = int(input())


def collatz(n):
    print(int(n), end=" ")
    if n == 1:
        return 1
    elif n % 2 == 0:
        collatz(n/2)
    else:
        collatz(n*3+1)

collatz(a)

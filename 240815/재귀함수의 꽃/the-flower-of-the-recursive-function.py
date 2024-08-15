n = int(input())


def printStar(n):
    if n == 0:
        return
    print(n, end=' ')
    printStar(n - 1)
    print(n, end=' ')


printStar(n)
n = int(input())


def printStar(n):
    if n == 0:
        return
    print('* ' * n)
    printStar(n - 1)
    print('* ' * n)


printStar(n)
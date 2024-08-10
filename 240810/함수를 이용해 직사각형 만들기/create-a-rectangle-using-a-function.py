def printStart(n,m):
    for i in range(n):
        print('1' * m)


n,m = map(int,input().split(' '))
printStart(n,m)
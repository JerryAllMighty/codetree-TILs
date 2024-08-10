def printNum(n):
    if n ==0:
        return
    printNum(n-1)
    print(n, end=' ')

def printNumBackward(n):
    if n ==0:
        return
    print(n, end=' ')
    printNumBackward(n-1)



n = int(input())
printNum(n)
print()
printNumBackward(n)
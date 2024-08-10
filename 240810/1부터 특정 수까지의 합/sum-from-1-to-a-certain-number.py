def sumN(n):
    num = 0
    for i in range(1,n+1):
        num += i
    return num
n = int(input())
print(sumN(n)//10)
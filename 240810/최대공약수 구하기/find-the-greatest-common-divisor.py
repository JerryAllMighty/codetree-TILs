def yaksu(n,m):
    temp = []
    for i in range(1,max(n,m)+1):
        if n % i == 0 and m % i == 0:
            temp.append(i)

    return max(temp)


n,m = map(int,input().split(' '))
print(yaksu(n,m))
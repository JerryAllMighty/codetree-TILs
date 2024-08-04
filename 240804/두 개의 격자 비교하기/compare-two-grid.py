n, m = map(int, input().strip().split(' '))

lst1 = [
    list(map(int,input().strip().split(' ')))
    for _ in range(n)

]

lst2 = [
    list(map(int,input().strip().split(' ')))
    for _ in range(n)

]
answers = []
for i in range(n):
    temp = []
    for j in range(m):
        if lst1[i][j] == lst2[i][j]:
            temp.append(0)
        else:
            temp.append(1)
    print(*temp)
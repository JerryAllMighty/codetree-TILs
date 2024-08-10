def printStart(n):
    num = 1
    for i in range(n):
        temp = []
        for j in range(n):
            if num >= 10:
                num = 1
            temp.append(num)
            num += 1

        print(*temp)


n = int(input())
printStart(n)
n = int(input())

lst = [
    [0 for i in range(1, n + 1)]
    for _ in range(n)
]
num = 0
startRow = n
startCol = n - 1
opposite = False
cnt = 0
while(cnt < n):
    if opposite is False:
        for j in range(startRow - 1, -1, -1):
            num += 1
            lst[j][startCol] = num
        opposite = True
        startCol -= 1
    else:
        for j in range(startRow):
            num += 1
            lst[j][startCol] = num

        opposite = False
        startRow = n
        startCol -=1

    cnt += 1

for i in lst:
    print(*i)